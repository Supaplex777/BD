from sqlalchemy import Column, Integer, String, Float
from db import Base, engine

class User(Base):
    __tablename__ = 'the_main' # когда меняешь имя меняется и таблица
    id = Column(Integer, primary_key=True) # primary первичный ключ 
    direction = Column(Integer) # направление
    course_name = Column(String) #название курсов
    school_name = Column(Integer) #имя школы
    the_cost = Column(Integer) # стоимость
    appraisal = Column(Float) # оценка
    link = Column(String(400), unique=True) # уникальна не может быть одинаковой ссылки

    def __repr__(self):
        return f"User {self.name}, {self.the_cost}"

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)  