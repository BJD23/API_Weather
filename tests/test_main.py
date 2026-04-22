from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_health_check():
    """
    Verifica que el endpoint de salud responde correctamente
    con un código 200 y el mensaje esperado.
    """
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "message": "La API está funcionando correctamente"}
