from db import db_session
from db.models_2 import User


user = User(direction='П')
db_session.add(user)
db_session.commit()

