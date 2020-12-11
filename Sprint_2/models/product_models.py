from pydantic import BaseModel
from typing import Dict

class ProductOut(BaseModel):
    Nombre: str
    Precio: int

class ProductCant(BaseModel):
    Nombre: str
    Disponibilidad: int
    
class ComProd(BaseModel):
    Nombre: str #Nombre del producto
    comentario: str
    email: str
    
database_comments = Dict[str, ComProd] #Diccionario
##Los asteriscos son para crear metodos en los cuales se dice que van parametros pero no se sabe cuantos son
database_comments = {}
    
def create_comment(item:ComProd):
    database_comments[item.Nombre] = item
    return True