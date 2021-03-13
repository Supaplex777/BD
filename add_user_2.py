from db import db_session
from models_2 import User 

user = User(direction='Программирование')
db_session.add(user)
db_session.commit()