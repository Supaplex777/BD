# получение через repr
from models import User

user = User.query.first()
print(user)