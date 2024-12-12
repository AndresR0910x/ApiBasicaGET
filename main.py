from fastapi import FastAPI, HTTPException
from Schema.users import IntegranteSchema
from database import session
from models.integrantes import Integrantes

app = FastAPI()

#Metodo get para obtener los datos
@app.get("/integrantes")
def read_root():
    
    #Traer todos los datos de la base de datos
    integrantes = session.query(Integrantes).all()
    
    if not integrantes:
        raise HTTPException(status_code=404, detail="No users found")
    
    #Cambiar el formato de los datos a JSON
    return [IntegranteSchema.model_validate(integrante).dict() for integrante in integrantes]