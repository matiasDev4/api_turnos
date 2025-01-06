from sqlalchemy import Column, Integer, String, Boolean
from config.database import base


class Dates_db(base):
    __tablename__ = "dates"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(250), nullable=False)
    date = Column(String(250), nullable=False)
    hours = Column(String(250), nullable=False)
    is_active = Column(Boolean, nullable=False)

class dates_aviality(base):
    __tablename__ = "aviality"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    day = Column(String(250), nullable=False)
    date = Column(String(250), nullable=False)
    hours = Column(String(250), nullable=False)
    is_active = Column(Boolean, nullable=False)