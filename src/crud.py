from sqlalchemy.orm import Session
from src import models, schemas

def get_usuario_by_email(db: Session, email: str):
    return db.query(models.Usuario).filter(models.Usuario.email == email).first()

def create_usuario(db: Session, usuario: schemas.UsuarioCreate):
    db_usuario = models.Usuario(
        nombre=usuario.nombre,
        email=usuario.email,
        unidad_medida=usuario.unidad_medida,
        activo=usuario.activo
    )
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def get_usuario(db: Session, usuario_id: int):
    return db.query(models.Usuario).filter(models.Usuario.id == usuario_id).first()

def create_favorito(db: Session, favorito: schemas.UbicacionFavoritaCreate):
    db_favorito = models.UbicacionFavorita(
        usuario_id=favorito.usuario_id,
        ciudad=favorito.ciudad,
        lat=favorito.lat,
        lon=favorito.lon
    )
    db.add(db_favorito)
    db.commit()
    db.refresh(db_favorito)
    return db_favorito
