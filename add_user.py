from db import db_session # добавление записи в базу данных Основная
from models import User 

user=User(direction=1, course_name='Профессия Веб-разработчик', school_name=1, the_cost=147500, appraisal= 4.4,link='https://skillbox.ru/course/profession-webdev/?utm_source=advcake&utm_medium=cpa&utm_campaign=affiliate&utm_content=exkentbkru&utm_term=d9eeb682da829916712a146f373e0d96&advcake_params=d9eeb682da829916712a146f373e0d96&sub1=baza')
db_session.add(user)
db_session.commit()