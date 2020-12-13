from db.products_db import ProductInDB, get_product, create_product,obtain_products, update_product
from db.users_db import UsersInDB, create_user, update_user
from db.comments_db import create_comment
from models.product_models import ProductOut, ProductCant
from models.comment_models import ComProdIn
from fastapi import FastAPI, HTTPException

api = FastAPI()

#Bienvenida
@api.get("/")
async def home():
    return {"message":"Bienvenido a la API de Tienda Virtual."}


####PRODUCTOS
#Obtener resumen del producto
@api.get("/api/v1/producto/{Nombre}")
async def resumen_producto(Nombre: str):
    product_in_db = get_product(Nombre)
    if product_in_db == None:
        raise HTTPException(status_code=404, detail="El producto no existe.")
    product_out = ProductOut(**product_in_db.dict())
    return  product_out

#Creación de productos
@api.post("/api/v1/producto", status_code=201)
async def crear_productos(product:ProductInDB):
    operacion_exitosa=create_product(product)
    if operacion_exitosa:
        return {"Producto creado": True}
    else:
        raise HTTPException(status_code=404,detail='El producto ya existe.')

#Obtener nombre y cantidad disponible
@api.get("/api/v1/producto/cantidad/{Nombre}")
async def obtener_cantidad(Nombre: str):
    product_in_db = get_product(Nombre)
    if product_in_db == None:
        raise HTTPException(status_code=404, detail="El producto no existe.")
    product_cant = ProductCant(**product_in_db.dict())
    return  product_cant

#Actualizar
@api.put("/api/v1/producto/actualizacion")
async def actualizar_productos(product:ProductInDB):
        actualizacion_exitosa=update_product(product)
        if actualizacion_exitosa:
            return {"Articulo actualizado":True}
        else:
            raise HTTPException(status_code=404,detail='El producto no existe.')

#Visualizar completo
@api.get("/api/v1/productos")
async def lista_productos():
    return obtain_products()
        
#####Usuarios        
#Creación de usuario
@api.post("/api/v1/usuario", status_code=201)
async def crear_usuarios(user:UsersInDB):
    operacion_exitosa = create_user(user)
    if operacion_exitosa:
        return {"Usurio creado": True}
    else:
        raise HTTPException(status_code=404,detail='El usuario ya existe.')
    
#Actualizar usuario
@api.put("/api/v1/usuario/actualizacion")
async def actualizar_usuarios(user:UsersInDB):
        actualizacion_exitosa=update_user(user)
        if actualizacion_exitosa:
            return {"Usuario actualizado": True}
        else:
            raise HTTPException(status_code=404,detail='El usuario no existe.')

#Creación de comentario
@api.post("/api/v1/comentario", status_code=201)
async def crear_comentarios(items:ComProdIn):
    operacion_exitosa=create_comment(items)
    if operacion_exitosa:
        return {"Comentario creado": True}
    else:
        raise HTTPException(status_code=404,detail='El producto no existe.')
