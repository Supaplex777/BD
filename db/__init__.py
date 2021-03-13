from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base #формат 
from sqlalchemy.orm import scoped_session, sessionmaker
# создать postgres://имяпароль@название хоста:порт/навзание базы данных
engine = create_engine('sqlite:///test.sqlite3')
db_session = scoped_session(sessionmaker(bind=engine)) # создаем сессию

Base = declarative_base() #модели будут наследоваться от Base
Base.query = db_session.query_property() # так удобнее 