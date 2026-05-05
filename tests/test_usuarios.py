from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.main import app
from src.database import get_db, Base
from src.schemas import UnidadMedidaEnum

# Configurar base de datos SQLite para pruebas locales y rápidas
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Sobrescribir dependencia de BD
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def setup_module(module):
    Base.metadata.create_all(bind=engine)

def teardown_module(module):
    Base.metadata.drop_all(bind=engine)

def test_create_usuario():
    response = client.post(
        "/usuarios",
        json={"nombre": "Test User", "email": "test@example.com", "unidad_medida": "metric", "activo": True}
    )
    assert response.status_code == 201, response.text
    data = response.json()
    assert data["nombre"] == "Test User"
    assert data["email"] == "test@example.com"
    assert "id" in data

def test_create_usuario_duplicate_email():
    # Intentar crear con el mismo correo del test anterior
    response = client.post(
        "/usuarios",
        json={"nombre": "Test User 2", "email": "test@example.com", "unidad_medida": "imperial", "activo": True}
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "El correo electrónico ya está registrado"

def test_create_usuario_invalid_email():
    response = client.post(
        "/usuarios",
        json={"nombre": "Invalid Email", "email": "invalid_email_format", "unidad_medida": "metric", "activo": True}
    )
    assert response.status_code == 422 # Error de validación de Pydantic
