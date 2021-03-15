from db import db_session
from models_4 import User


user = User(scholl='Convert Monster')
db_session.add(user)
db_session.commit()