from sqlalchemy import Column, Integer, String, Float
from db import Base, engine

class User(Base):
    __tablename__ = 'skill' # когда меняешь имя меняется и таблица
    id = Column(Integer, primary_key=True) # primary первичный ключ 
    skill = Column(String) # навыки
    
    def __repr__(self):
        return f"User {self.name}, {self.the_cost}"

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)  