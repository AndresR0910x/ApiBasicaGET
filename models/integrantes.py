from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from database import engine, session
from sqlalchemy.engine import URL


Base = declarative_base()


# Creacion de la tabla para la base de datos
class Integrantes(Base):
    __tablename__ = 'estudiantes'
    id = Column(Integer, primary_key=True)
    name = Column(String)


Base.metadata.create_all(engine)

print("Tabla para los 'integrantes' creada exitosamente.")
