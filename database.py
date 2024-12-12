from sqlalchemy import create_engine, inspect
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError


# Database connection details
url = URL.create(
    drivername="postgresql",
    username="postgres",
    password="",
    host="localhost",
    database="Integrantes",
    port=5432
)


# Create engine
engine = create_engine(url)

Session = sessionmaker(bind=engine)
session = Session()
