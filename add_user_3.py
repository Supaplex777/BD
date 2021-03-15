from db import db_session
from models_3 import User


user = User(skill='Машинное обучение')
db_session.add(user)
db_session.commit()