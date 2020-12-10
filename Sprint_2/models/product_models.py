from pydantic import BaseModel

class ProductOut(BaseModel):
    Nombre: str
    Precio: int

class ProductCant(BaseModel):
    Nombre: str
    Disponibilidad: int