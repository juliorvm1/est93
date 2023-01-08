"""
archivo para mantener la configuración de conexión a la base de datos
"""

from sqlalchemy import create_engine, MetaData


engine=create_engine("mysql+pymysql://uEst93:ianr@localhost:3306/dbEst93")
meta=MetaData()
conn=engine.connect()