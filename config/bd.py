from sqlalchemy import create_engine, MetaData



engine=create_engine("mysql+pymysql://uEst93:ianr@localhost:3306/dbEst93")
meta=MetaData()
conn=engine.connect()