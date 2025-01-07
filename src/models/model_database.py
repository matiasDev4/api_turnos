from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from config.database import base


class Dates_db(base):
    __tablename__ = "dates"

    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(String(250), nullable=False)
    rel_hour = relationship("Hours")

class Hours(base):
    __tablename__ = "hours"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    hour = Column(String(250), nullable=False)
    date_unique = Column(Integer, ForeignKey("dates.date"))
    rel_hour = relationship("User")
    
class User(base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String(250), nullable=False)
    user_email = Column(String(250), nullable=False)
    user_pay_status = Column(String(250), nullable=False)
    date_selected = Column(String(250), nullable=False)
    hour_selected = Column(String(250), ForeignKey("hours.hour"))
    