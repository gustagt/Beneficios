from sqlalchemy import create_engine

db_connect = create_engine('mysql+mysqldb://beneficios:transcon#123@10.101.22.36:3306/beneficios')

print(db_connect.connect())