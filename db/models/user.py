from sqlalchemy import Column, Integer, String
from db.db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer, unique=True, nullable=False)
    gender = Column(String)
    name = Column(String)
    character_class = Column(String)