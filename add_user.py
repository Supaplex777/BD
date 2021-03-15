from db import db_session # добавление записи в базу данных Основная
from models import Main 

first=Main(direction=1, course_name='Профессия Веб-разработчик', school_name=1, the_cost=147500, appraisal= 4.4,link='https://skillbox.ru/course/profession-webdev/?utm_source=advcake&utm_medium=cpa&utm_campaign=affiliate&utm_content=exkentbkru&utm_term=b5f8e8688d44facf7038ddd31729feff&advcake_params=b5f8e8688d44facf7038ddd31729feff&sub1=baza')
db_session.add(first)
db_session.commit()