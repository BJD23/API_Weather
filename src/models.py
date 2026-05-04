from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from src.database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    fecha_registro = Column(TIMESTAMP, server_default=func.now())

    ubicaciones = relationship("UbicacionFavorita", back_populates="usuario")


class UbicacionFavorita(Base):
    __tablename__ = "ubicaciones_favoritas"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    ciudad = Column(String(100), nullable=False)

    usuario = relationship("Usuario", back_populates="ubicaciones")
