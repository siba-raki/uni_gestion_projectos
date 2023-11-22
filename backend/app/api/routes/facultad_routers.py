from fastapi import APIRouter, HTTPException, status, Depends
from typing import List
from sqlalchemy.orm import Session
from ...schemas.facultad import FacultadCreate
from ...schemas.facultad import Facultad as FacultadSchema
from ...models.facultad import Facultad as FacultadModel
from ...database.session import get_db

router = APIRouter()
@router.post("/facultades/", response_model=FacultadCreate, status_code=status.HTTP_201_CREATED)
def create_facultad(facultad_data: FacultadCreate, db: Session = Depends(get_db)):
    nueva_facultad = FacultadModel(**facultad_data.dict())

    db.add(nueva_facultad)
    db.commit()
    db.refresh(nueva_facultad)

    return nueva_facultad

@router.get("/facultades/", response_model=List[FacultadSchema])
def read_facultades(db: Session = Depends(get_db)):
    facultades = db.query(FacultadModel).all()
    return facultades