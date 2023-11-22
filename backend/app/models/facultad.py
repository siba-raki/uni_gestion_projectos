from sqlalchemy import Column, Integer, String, DateTime, func, Boolean
from .base import Base

class Facultad(Base):
    __tablename__ = 'Facultad'

    id = Column(Integer, primary_key=True, index=True)
    descripcion = Column(String, nullable=False)
    fecha_creacion = Column(DateTime, default=func.now(), nullable=False)
    fecha_modificacion = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=True)
    is_active = Column(Boolean, default=True)
    # ? estado_id_bigint = Column(Integer, nullable=False)
