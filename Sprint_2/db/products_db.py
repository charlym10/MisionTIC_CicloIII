from typing import Dict
from pydantic import BaseModel

class ProductInDB(BaseModel): #Public class UserInDB exends BaseModel
    Nombre: str
    Categoría: str
    Precio: int
    Unidad: str
    Proveedor: str
    Disponibilidad: int
    
#Segundo bloque
    
database_products = Dict[int, ProductInDB] #Diccionario
##Los asteriscos son para crear metodos en los cuales se dice que van parametros pero no se sabe cuantos son
database_products = {
    'GS1- Camara NIKON Profesional D-5300 + Estuche + SD 16 GB Negra':ProductInDB(**{'Nombre': 'GS1- Camara NIKON Profesional D-5300 + Estuche + SD 16 GB Negra',
                                                                                'Categoría': 'Cámaras',
                                                                                'Precio': 2829900,
                                                                                'Unidad': 'Und',
                                                                                'Proveedor': 'COLOMBIANA DE COMERCIO S.A Y/O ALKOSTO S.A',
                                                                                'Disponibilidad':10}),
    'GS1- Nevera Minibar Duplex ABBA NVARS113B 2 Puertas Frost  87 Litros  Blanco': ProductInDB(**{'Nombre': 'GS1- Nevera Minibar Duplex ABBA NVARS113B 2 Puertas Frost  87 Litros  Blanco',
                'Categoría': 'Neveras',
                'Precio': 774900.00,
                'Unidad': 'Und',
                'Proveedor': 'COLOMBIANA DE COMERCIO S.A Y/O ALKOSTO S.A',
                'Disponibilidad':10}),
    'GS1- Cartucho de tinta HP 662 negra Original CZ103AL': ProductInDB(**{'Nombre': 'GS1- Cartucho de tinta HP 662 negra Original CZ103AL',
                'Categoría': 'Accesorios',
                'Precio': 51500.00,
                'Unidad': 'Und', 
                'Proveedor': 'COLOMBIANA DE COMERCIO S.A Y/O ALKOSTO S.A',
                'Disponibilidad':10}),
    'GS1- Cartucho de tinta HP 662 Tricolor Original CZ104AL': ProductInDB(**{'Nombre': 'GS1- Cartucho de tinta HP 662 Tricolor Original CZ104AL',
                'Categoría': 'Accesorios',
                'Precio': 51500.00, 
                'Unidad': 'Und',
                'Proveedor': 'COLOMBIANA DE COMERCIO S.A Y/O ALKOSTO S.A',
                'Disponibilidad':10}),
    'GS1- Soporte Base con inclinacion LCD   LED   PLASMA 40"A 46" ST-WTV-33T': ProductInDB(**{'Nombre': 'GS1- Soporte Base con inclinacion LCD   LED   PLASMA 40"A 46" ST-WTV-33T',
                'Categoría': 'Accesorios',
                'Precio': 74900.00,
                'Unidad': 'Und',
                'Proveedor': 'COLOMBIANA DE COMERCIO S.A Y/O ALKOSTO S.A',
                'Disponibilidad':10}),
    'MESA BANQUETE LIFETIME 1.52CM': ProductInDB(**{'Nombre': 'MESA BANQUETE LIFETIME 1.52CM',
                'Categoría': 'Mesas oficina',
                'Precio': 179900.00,
                'Unidad': 'Und',
                'Proveedor': 'MAKRO SUPERMAYORISTA S.A.S',
                'Disponibilidad':10}),
    'SILLA CONTEMPORANEA LIFETIME 80191':ProductInDB(**{'Nombre': 'SILLA CONTEMPORANEA LIFETIME 80191',
                'Categoría': 'Sillas oficina',
                'Precio': 79900.00, 
                'Unidad': 'Und',
                'Proveedor': 'MAKRO SUPERMAYORISTA S.A.S',
                'Disponibilidad':10}),
    'GS1- Soporte para TV de Brazo TECHNOSOPORTES Esqualizable 37" a 60"': ProductInDB(**{'Nombre': 'GS1- Soporte para TV de Brazo TECHNOSOPORTES Esqualizable 37" a 60"',
                'Categoría': 'Accesorios', 
                'Precio': 119900.00,
                'Unidad': 'Und',
                'Proveedor': 'COLOMBIANA DE COMERCIO S.A Y/O ALKOSTO S.A',
                'Disponibilidad':10})
    
}


#Tercer bloque:
def get_product(Nombre: str):
    if Nombre in database_products.keys():
        return database_products[Nombre]
    else:
        return None
    
def create_product(product:ProductInDB):
    if product.Nombre in database_products.keys():
        return False
    else:
        elemento = {
            product.Nombre: product
        }
        
        database_products.update(elemento)
        
        return True
    
def update_product(product_in_db: ProductInDB):
    if product_in_db.Nombre in database_products.keys():
        elemento = {
            product_in_db.Nombre: product_in_db
        }
        
        database_products.update(elemento)
    else:
        return False
    
    return product_in_db

def obtain_products():
    return database_products

    
