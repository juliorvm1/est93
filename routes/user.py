"""
Archivo que sirve para agrupar los Endpoints relacionados a los usuarios con las operaciones
CRUD para poder manipular la base de datos y hacer las consultas
"""

from cryptography.fernet import Fernet
from schemas.user import User
from config.bd import conn
from models.users import t_users
from fastapi import APIRouter, Response, status,HTTPException
from starlette.status import HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND
from typing import List
user = APIRouter()
key = Fernet.generate_key()
f = Fernet(key)

# ruta para obtener todos los registros de la tabla t_users


@user.get("/users",response_model=List[User],tags=["Users"])
def get_users():
    return conn.execute(t_users.select()).fetchall()

# ruta para insertar un registro la tabla t_users


@user.post("/users",response_model=User,tags=["Users"])
def create_user(nuser: User):
    new_user = {"name": nuser.name, "email": nuser.email}
    new_user["password"] = f.encrypt(nuser.password.encode("utf-8"))
    result = conn.execute(t_users.insert().values(new_user))
    return conn.execute(t_users.select().where(t_users.c.id == result.lastrowid)).first()

# ruta pa consultar un registro de la tabla t_users usando como parametro el id del usuario


@user.get("/users/{id}",response_model=User,tags=["Users"])
def get_userByid(id: str):
    result= conn.execute(t_users.select().where(t_users.c.id == id)).first()    
    if  not result:
        #return status.HTTP_404_NOT_FOUND
        #print (result)
        raise HTTPException(status_code=404, detail="User not found")
    else:
        return result
        


# ruta para hacer la eliminación de un registro de la tabla t_users usando como parametro el id
@user.delete("/users/{id}",status_code=status.HTTP_204_NO_CONTENT,tags=["Users"])
def delete_userByid(id: str):
    result = conn.execute(t_users.delete().where(t_users.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)

# ruta para actualizar un registro de la tabla t_users usando como paramtro el id


@user.put("/users/{id}", response_model=User,tags=["Users"])
def update_user(id: str, uuser: User):
    result = conn.execute(t_users.update().values(
        name=uuser.name, email=uuser.email, password=f.encrypt(uuser.password.encode("utf-8"))).where(t_users.c.id==id))
    return conn.execute(t_users.select().where(t_users.c.id==id)).first()