from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class UbicacionFavoritaBase(BaseModel):
    ciudad: str

class UbicacionFavoritaCreate(UbicacionFavoritaBase):
    pass

class UbicacionFavorita(UbicacionFavoritaBase):
    id: int
    usuario_id: int

    class Config:
        from_attributes = True

class UsuarioBase(BaseModel):
    nombre: str

class UsuarioCreate(UsuarioBase):
    pass

class Usuario(UsuarioBase):
    id: int
    fecha_registro: datetime
    ubicaciones: List[UbicacionFavorita] = []

    class Config:
        from_attributes = True
