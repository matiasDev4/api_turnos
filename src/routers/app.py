from fastapi.routing import APIRouter
from fastapi import Depends
from config.database import base, engine, session
from sqlalchemy.orm import Session
import json
import os

app_route = APIRouter()

base.metadata.create_all(bind=engine)

def get_date():
    db = session()
    try:
        yield db
    finally:
        db.close()


@app_route.get("/availability_dates")
async def get_date(db: Session = Depends(get_date)):
    if os.path.exists(os.getcwd() + "/dates/dates.json"):
        with open (os.getcwd() + "/dates/dates.json", "r", encoding="utf-8") as file:
            json_file = json.load(file)
            for x in json_file:
                consult = db.execute("SELECT * FROM dates WHERE date = :date", {"date": x["date"]}).fetchall()
                return consult
    else:
        return {"message": "No hay fechas disponibles"}