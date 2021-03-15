from db import db_session
from models_5 import User

user = User(definition_of_skill='П')
db_session.add(user)
db_session.commit()