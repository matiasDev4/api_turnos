from fastapi.routing import APIRouter
from fastapi import Depends
from config.database import base, engine, session
from sqlalchemy.orm import Session
from schemas.schema_shift import ShiftBase
from models.model_database import Dates_db
import json
import os

app_route = APIRouter()

Dates_db.metadata.create_all(bind=engine)

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()


@app_route.get("/availability_dates")
async def get_date(db: Session = Depends(get_db)):
    with open (os.getcwd() + "/modules/dates/dates.json", "r", encoding="utf-8") as file:
        json_file = json.load(file)
        for x in json_file["dates"]:
            for entry in x["date"]:
                consult = db.query(Dates_db).filter(Dates_db.date==entry).all()
                return consult


@app_route.post("/create_dates")
def create_date(dates: ShiftBase, db: Session = Depends(get_db)):
    insert = Dates_db(id=dates.id, name=dates.name, date=dates.date, hours=dates.hour, is_active=dates.is_active)
    db.add(insert)
    db.commit()
    db.refresh(insert)
    return {"message": "Fecha creada con exito"}
