from sqlalchemy import column, Integer, String
from src.config.database import base


class Dates_db(base):
    __tablename__ = "dates"

    id = column(Integer, primary_key=True)
    date = column(String, nullable=False)
    hours = column(String, nullable=False)