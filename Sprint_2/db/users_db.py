
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
    if user.Usuario in database_users.keys():
        return False
    else:
        elemento = {
            user.Usuario: user
        }
        
        database_users.update(elemento)
        
        return True

def update_user(users_in_db: UsersInDB):
    if users_in_db.Usuario in database_users.keys():
        elemento = {
            users_in_db.Usuario: users_in_db
        }
        
        database_users.update(elemento)
    else:
        return False
    
    return users_in_db

#Prueba