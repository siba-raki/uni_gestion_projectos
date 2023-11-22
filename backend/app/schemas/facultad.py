from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Esquema base para Facultad, para operaciones de lectura
class FacultadBase(BaseModel):
    descripcion: str

# Esquema para crear una Facultad, validaciones
class FacultadCreate(FacultadBase):
    pass

# Esquema para la respuesta de Facultad
class Facultad(FacultadBase):
    id: int
    descripcion: str
    fecha_creacion: datetime
    fecha_modificacion: Optional[datetime]

    class Config:
        from_attributes  = True