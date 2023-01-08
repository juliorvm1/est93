"""
Archivo para crear desde python la tabla t_users con la estructura necesaria
"""
from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.bd import engine, meta

t_users=Table("t_users",meta,
              Column("id", Integer, primary_key=True),
              Column("name",String(255)),
              Column("email", String(255)),
              Column("password", String(255)))
meta.create_all(engine)
