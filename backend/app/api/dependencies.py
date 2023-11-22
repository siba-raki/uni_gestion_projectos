from sqlalchemy.orm import Session
from ..database.session import get_db

# Dependencia para obtener la sesión de la base de datos
def get_database_session(db: Session = Depends(get_db)):
    try:
        yield db
    finally:
        db.close()
