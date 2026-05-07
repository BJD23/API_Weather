from unittest.mock import patch, AsyncMock
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.main import app
from src.database import get_db
from src.models import Base

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def test_health_check():
    """
    Verifica que el endpoint de salud responde correctamente
    con el nuevo formato detallado.
    """
    with patch("src.services.weather.check_api_status", new_callable=AsyncMock) as mock_weather:
        # Configuramos el mock para que devuelva éxito
        mock_weather.return_value = (True, "Conectado")
        
        response = client.get("/health")
        assert response.status_code == 200
        
        data = response.json()
        assert data["status"] == "ok"
        assert "services" in data
        assert data["services"]["api"] == "healthy"
        assert data["services"]["database"] == "healthy"
        assert data["services"]["weather_api"] == "healthy"

def test_create_favorito():
    # Registrar un usuario primero
    user_data = {
        "nombre": "UserFav",
        "email": "userfav@example.com",
        "unidad_medida": "metric",
        "activo": True
    }
    response_user = client.post("/usuarios", json=user_data)
    assert response_user.status_code == 201
    user_id = response_user.json()["id"]

    # Agregar ubicación favorita para el usuario
    fav_data = {
        "ciudad": "Xalapa",
        "lat": 19.5312,
        "lon": -96.9159,
        "usuario_id": user_id
    }
    response_fav = client.post("/favoritos", json=fav_data)
    assert response_fav.status_code == 201
    assert response_fav.json()["ciudad"] == "Xalapa"
    assert response_fav.json()["usuario_id"] == user_id
    assert response_fav.json()["lat"] == 19.5312
    assert response_fav.json()["lon"] == -96.9159
