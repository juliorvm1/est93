"""
Archivo para mantener un esquema con los tipos de datos esperados para la clase User el cual 
representa un modelo esperado en la base de datos
"""
from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id:Optional[str]
    name:str
    email:str
    password: str
    