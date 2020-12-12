from db.products_db import ProductInDB
from db.users_db import UsersInDB
from db.products_db import get_product, create_product,obtain_products, update_product
from db.users_db import create_users, update_user, modify_user
from models.product_models import ProductOut, ProductCant,ComProd, create_comment
import datetime
from fastapi import FastAPI, HTTPException

api = FastAPI()
#Bienvenida
@api.get("/")
async def home():
    return {"message":"Bienvenido a su tienda virtual"}


####PRODUCTOS
#Obtener resumen del producto (Nombre y precio)
@api.get("/user/producto/{Nombre}")
async def resumen_producto(Nombre: str):
    product_in_db = get_product(Nombre)
    if product_in_db == None:
        raise HTTPException(status_code=404, detail="El producto no existe")
    product_out = ProductOut(**product_in_db.dict())
    return  product_out

#Creación de productos
@api.post("/items/")
async def crear_productos(product:ProductInDB):
    operacion_exitosa=create_product(product)
    if operacion_exitosa:
        return {"Ingresado": True}
    else:
        raise HTTPException(status_code=400,detail='ya creado')

#Obtener nombre y cantidad disponible
@api.get("/user/cantidad/{Nombre}")
async def obtener_cantidad(Nombre: str):
    product_in_db = get_product(Nombre)
    if product_in_db == None:
        raise HTTPException(status_code=404, detail="El producto no existe")
    product_cant = ProductCant(**product_in_db.dict())
    return  product_cant

#Actualizar
    
@api.put("/items/actualizacion")
async def actualizar_productos(product:ProductInDB):
        actualizacion_exitosa=update_product(product)
        if actualizacion_exitosa:
            return {"Articulo actualizado":True}
        else:
            raise HTTPException(status_code=400,detail='No se ha podido actualizar')

#Visualizar completo
@api.get("/productos")
async def lista_productos():
    return obtain_products()
        
#####Usuarios        
#Creación de usuarios
@api.post("/usuarios/")
async def crear_usuarios(user:UsersInDB):
    operacion_exitosa=create_users(user)
    if operacion_exitosa:
        return {"Usurio ya ingresado": True}
    else:
        raise HTTPException(status_code=400,detail='Usuario ya creado.')

#Creación de comentarios
@api.post("/comentarios/")
async def crear_comentarios(items:ComProd):
    operacion_exitosa=create_comment(items)
    if operacion_exitosa:
        return {"Comentario creado": True}
    else:
        raise HTTPException(status_code=400,detail='Ya creó su comentario')

#Modificacion de usuarios
@api.put("/usuarios/modificacion")
async def modificar_usuarios(user:UsersInDB):
        actualizacion_exitosa=modify_user(user)
        if actualizacion_exitosa:
            return {"Usuario modificado":True}
        else:
            raise HTTPException(status_code=400,detail='No se ha podido modificar')
#Actualizar usuarios
@api.put("/usuarios/actualizacion")
async def actualizar_usuarios(user:UsersInDB):
        actualizacion_exitosa=update_user(user)
        if actualizacion_exitosa:
            return {"usuario actualizado":True}
        else:
            raise HTTPException(status_code=400,detail='No se ha podido actualizar')
