import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, AsyncMock, MagicMock
from src.main import app

client = TestClient(app)

@patch("src.services.weather.httpx.AsyncClient.get")
def test_get_clima_success(mock_get):
    # Mocking the httpx response
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "name": "Xalapa",
        "main": {
            "temp": 20.5,
            "feels_like": 21.0,
            "humidity": 65
        },
        "weather": [{"description": "cielo claro"}],
        "wind": {"speed": 3.5}
    }
    mock_get.return_value = mock_response

    response = client.get("/clima/Xalapa")
    assert response.status_code == 200
    data = response.json()
    assert data["ciudad"] == "Xalapa"
    assert data["temperatura"] == 20.5
    assert data["descripcion"] == "Cielo claro"

@patch("src.services.weather.httpx.AsyncClient.get")
def test_get_clima_not_found(mock_get):
    mock_response = MagicMock()
    mock_response.status_code = 404
    mock_get.return_value = mock_response

    response = client.get("/clima/CiudadInexistente")
    assert response.status_code == 404
    assert "no encontrada" in response.json()["detail"]
