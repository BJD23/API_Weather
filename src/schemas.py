from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from typing import List, Optional
from enum import Enum

class UnidadMedidaEnum(str, Enum):
    metric = 'metric'
    imperial = 'imperial'

class UbicacionFavoritaBase(BaseModel):
    ciudad: str

class UbicacionFavoritaCreate(UbicacionFavoritaBase):
    pass

class UbicacionFavorita(UbicacionFavoritaBase):
    id: int
    usuario_id: int
    model_config = ConfigDict(from_attributes=True)

class UsuarioBase(BaseModel):
    nombre: str
    email: str = Field(pattern=r"^\S+@\S+\.\S+$")
    unidad_medida: UnidadMedidaEnum = UnidadMedidaEnum.metric
    activo: bool = True

class UsuarioCreate(UsuarioBase):
    pass

class Usuario(UsuarioBase):
    id: int
    fecha_registro: datetime
    ubicaciones: List[UbicacionFavorita] = []
    model_config = ConfigDict(from_attributes=True)
