from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src import models, schemas, crud
from src.database import engine, get_db
from src.services import weather

try:
    models.Base.metadata.create_all(bind=engine)
except Exception as e:
    print(f"Advertencia: No se pudo conectar a la base de datos MySQL durante el inicio. {e}")

app = FastAPI(
    title="API Weather - Proyecto Integrador",
    description="API RESTful para consultar el clima y guardar favoritos.",
    version="1.0.0"
)

@app.post("/usuarios", response_model=schemas.Usuario, status_code=status.HTTP_201_CREATED, tags=["Gestión de Usuarios"])
def create_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    db_usuario = crud.get_usuario_by_email(db, email=usuario.email)
    if db_usuario:
        raise HTTPException(status_code=400, detail="El correo electrónico ya está registrado")
    return crud.create_usuario(db=db, usuario=usuario)

@app.get("/usuarios/{id_usuario}", response_model=schemas.Usuario, tags=["Gestión de Usuarios"])
def get_usuario(id_usuario: int, db: Session = Depends(get_db)):
    db_usuario = crud.get_usuario(db, usuario_id=id_usuario)
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_usuario

@app.get("/health", tags=["Sistema"])
def check_health():
    return {"status": "ok", "message": "La API está funcionando correctamente"}

@app.get("/clima/{ciudad}", response_model=schemas.ClimaResponse, tags=["Gestión de Clima"])
async def get_clima(ciudad: str):
    return await weather.get_current_weather(ciudad)
