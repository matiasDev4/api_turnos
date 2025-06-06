from fastapi.routing import APIRouter
from fastapi.responses import JSONResponse
from fastapi import Depends
from config.database import base, engine, session
from sqlalchemy.orm import Session
from schemas.schema import ShiftBase
from models.model_database import Dates_db, Hours
import json
import os
from modules.class_ import crear_fecha
import datetime
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
    query = db.query(Dates_db).join(Hours.hour==Dates_db.rel_hour).all()
    return query


@app_route.post("/create_dates")
def create_date(db: Session = Depends(get_db)):
    fechas = crear_fecha()
    query = db.query(Dates_db).all()
    if query is None:
        for x in fechas:
            insert = Dates_db(dates_ = x)
            db.add(insert)
        db.commit()
        JSONResponse(content="Fechas creadas", status_code=201)
    else:
        JSONResponse(content="Esas fechas ya existen", status_code=200)
        

@app_route.post("/create_hours")
def create_hours(db: Session = Depends(get_db)):
    horas = crear_fecha()
    query = db.query(Dates_db).all()
    if query is None:
        for x in horas:
            insert = Dates_db(Hours)
            db.add(insert)
        db.commit()
        JSONResponse(content="Horas creadas", status_code=201)
    else:
        JSONResponse(content="Esas horas ya existen", status_code=200)
      