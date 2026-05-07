import httpx
from fastapi import HTTPException
from src.config import settings

async def get_current_weather(ciudad: str, units: str = "metric", lang: str = "es"):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": ciudad,
        "appid": settings.WEATHER_API_KEY,
        "units": units,
        "lang": lang
    }
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, params=params)
        except httpx.RequestError as exc:
            raise HTTPException(
                status_code=500, 
                detail=f"Error al contactar el servicio de clima: {str(exc)}"
            )
        
        if response.status_code == 404:
            raise HTTPException(status_code=404, detail=f"Ciudad '{ciudad}' no encontrada.")
        elif response.status_code == 401:
            raise HTTPException(status_code=500, detail="Error de autenticación con el servicio de clima. Verifique la API Key.")
        elif response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Error inesperado del servicio de clima.")
            
        data = response.json()
        
        return {
            "ciudad": data["name"],
            "temperatura": data["main"]["temp"],
            "sensacion_termica": data["main"]["feels_like"],
            "descripcion": data["weather"][0]["description"].capitalize(),
            "humedad": data["main"]["humidity"],
            "velocidad_viento": data["wind"]["speed"]
        }

async def check_api_status():
    """
    Verifica la conectividad y validez de la API Key con OpenWeatherMap.
    """
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": "London",
        "appid": settings.WEATHER_API_KEY
    }
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, params=params)
            if response.status_code == 200:
                return True, "Conectado"
            elif response.status_code == 401:
                return False, "API Key inválida o expirada"
            else:
                return False, f"Error del servicio externo: {response.status_code}"
        except Exception as e:
            return False, f"No se pudo contactar al proveedor: {str(e)}"
