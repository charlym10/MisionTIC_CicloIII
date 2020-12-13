from pydantic import BaseModel

class ComProdIn(BaseModel):
    IdProducto: str #Nombre del producto
    comentario: str
    email: str