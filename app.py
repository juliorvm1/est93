"""
Archvo principal que contiene la variable que representa la aplicación en el se incluyen
las rutas existentes en la aplicación como son los CRUDS para usuarios, pueden existir 
otras rutas
"""

from fastapi import FastAPI
from routes.user import user


app=FastAPI(title="Api est93",description="Api para gestionar cooperaciones sindicales",version="0.0.1",openapi_tags=[{"name":"Users","description":"user routes"}])
app.include_router(user)