from fastapi import APIRouter
user=APIRouter()
from models.users import t_users
from config.bd import conn
from schemas.user import User
from cryptography.fernet import Fernet
key=Fernet.generate_key()
f=Fernet(key)

@user.get("/users")
def get_users():
    return conn.execute(t_users.select()).fetchall()

@user.post("/users")
def create_user(nuser:User):
    new_user={"name":nuser.name,"email":nuser.email}    
    new_user["password"]=f.encrypt(nuser.password.encode("utf-8"))
    result=conn.execute(t_users.insert().values(new_user))
    return conn.execute(t_users.select().where(t_users.c.id==result.lastrowid)).first()
    
    