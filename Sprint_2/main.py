
from db.products_db import ProductInDB
from db.products_db import get_product, create_product
from models.product_models import ProductOut, ProductCant

import datetime
from fastapi import FastAPI, HTTPException

api = FastAPI()

@api.get("/")
async def home():
    return {"message":"Bienvenido"}

@api.get("/user/producto/{Nombre}")
async def get_product_char(Nombre: str):

    product_in_db = get_product(Nombre)
    if product_in_db == None:
        raise HTTPException(status_code=404, detail="El producto no existe")

    product_out = ProductOut(**product_in_db.dict())

    return  product_out

@api.post("/items/")
# async def crear_productos(item:ProductInDB):
#     create_product(item.Nombre, item.Categoría, item.Precio,
#                    item.Unidad, item.Proveedor)
#     return  {"Ingresado": True}


async def crear_productos(product:ProductInDB):
    operacion_exitosa=create_product(product)
    if operacion_exitosa:
        return {"Ingresado": True}
    else:
        raise HTTPException(status_code=400,detail='ya creado')
        

@api.get("/user/cantidad/{Nombre}")
async def get_product_cant(Nombre: str):

    product_in_db = get_product(Nombre)
    if product_in_db == None:
        raise HTTPException(status_code=404, detail="El producto no existe")

    product_cant = ProductCant(**product_in_db.dict())

    return  product_cant
