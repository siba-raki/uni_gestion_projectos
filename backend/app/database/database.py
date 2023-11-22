from sqlalchemy.ext.declarative import declarative_base
from databases import Database
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
DATABASE_URL = os.environ.get('database_url')

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

database = Database(DATABASE_URL)

Base = declarative_base()
