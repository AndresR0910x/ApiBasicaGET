from pydantic import BaseModel
from models.integrantes import Integrantes

class IntegranteSchema(BaseModel):
    id: int
    name: str
    
    class Config:
        from_attributes = True
        
        