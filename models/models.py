from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Movie(Base):
    __tablename__ = 'my_movies'
    id = Column(Integer, primary_key=True, index=True)
    author = Column(String, index=True)
    description = Column(String)
    release_date = Column(Date)
