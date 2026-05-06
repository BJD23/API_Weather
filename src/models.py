from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey, Boolean, Enum, DECIMAL
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from src.database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, index=True, nullable=False)
    unidad_medida = Column(Enum('metric', 'imperial'), server_default='metric')
    fecha_registro = Column(TIMESTAMP, server_default=func.now())
    activo = Column(Boolean, server_default='1')

    ubicaciones = relationship("UbicacionFavorita", back_populates="usuario")


class UbicacionFavorita(Base):
    __tablename__ = "ubicaciones_favoritas"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    ciudad = Column(String(100), nullable=False)
    lat = Column(DECIMAL(10, 8), nullable=False)
    lon = Column(DECIMAL(11, 8), nullable=False)

    usuario = relationship("Usuario", back_populates="ubicaciones")
