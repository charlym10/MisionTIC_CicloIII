
from typing import Dict
from pydantic import BaseModel
class UsersInDB(BaseModel): #Public class UserInDB exends BaseModel
    Usuario: str
    Nombre: str
    Apellido: str
    Password: str
    Rol: str
    Estado: str
    
#Segundo bloque
    
database_users = Dict[str, UsersInDB] #Diccionario
##Los asteriscos son para crear metodos en los cuales se dice que van parametros pero no se sabe cuantos son
database_users = {
'moagomezma':UsersInDB(**{'Usuario': 'moagomezma',
                          'Nombre': 'Monica',
                          'Apellido': 'Gomez',
                          'Password': '123456',
                          'Rol': 'Empleada',
                          'Estado':'Activo'}),
'usuario':UsersInDB(**{'Usuario': 'usuario1',
                          'Nombre': 'usuario',
                          'Apellido': 'us',
                          'Password': '000000',
                          'Rol': 'Cliente',
                          'Estado': 'Activo'})
}

def create_user(user:UsersInDB):
    if user.usuario in database_users:
        return False
    else:
        database_users[user.usuario] = user
        return True

def update_product(users_in_db: UsersInDB):
    database_users[users_in_db.Nombre] = users_in_db
    return users_in_db

def modify_user(users_in_db: UsersInDB):
    database_users[users_in_db.Nombre] = users_in_db
    return users_in_db