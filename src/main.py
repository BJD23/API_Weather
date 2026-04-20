from fastapi import FastAPI

app = FastAPI(
    title="API Weather - Proyecto Integrador",
    description="API RESTful para consultar el clima y guardar favoritos.",
    version="1.0.0"
)

@app.get("/health", tags=["Sistema"])
def check_health():
    return {"status": "ok", "message": "La API está funcionando correctamente"}
