from pydantic import BaseModel
from typing import Dict
from .products_db import database_products

class ComProd(BaseModel):
    IdProducto: str #Nombre del producto
    comentario: str
    email: str

database_comments = Dict[str, ComProd] #Diccionario
##Los asteriscos son para crear metodos en los cuales se dice que van parametros pero no se sabe cuantos son
database_comments = {}

index: int = 0

def create_comment(item: ComProd):
    if item.IdProducto in database_products.keys():
        global index
        index += 1
        
        elemento = {
            item.IdProducto: item
        }
        
        database_comments.update(elemento)
    else:
        return False
    return True