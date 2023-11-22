import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .core.config import settings
from .api.routes import facultad_router
from .database.database import Base, engine, database
from .models.facultad import Facultad


app = FastAPI(
    title='API',
    description="API para el software de gestion de bibliografias",
    version="1.0.0",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# * rutas
app.include_router(facultad_router)

def create_tables():
    Base.metadata.create_all(bind=engine)

@app.on_event("startup")
async def startup_event():
    await database.connect()
    create_tables()

@app.on_event("shutdown")
async def shutdown_event():
    await database.disconnect()