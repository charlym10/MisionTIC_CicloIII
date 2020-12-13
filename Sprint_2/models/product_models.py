from pydantic import BaseModel
from typing import Dict
from db.products_db import database_products

class ProductOut(BaseModel):
    Nombre: str
    Categoría: str
    Precio: int
    Unidad: str
    Proveedor: str
    Disponibilidad: int

class ProductCant(BaseModel):
    Nombre: str
    Disponibilidad: int
