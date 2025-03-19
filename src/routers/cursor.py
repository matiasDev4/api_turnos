from fastapi.routing import APIRouter
from fastapi import Depends, Form , HTTPException, UploadFile
from fastapi.responses import FileResponse
from config.database import session
from sqlalchemy.orm import Session
from models.model_database import Courses
from schemas.schema import Courser_schema
import os

app_cursos = APIRouter()



def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

@app_cursos.get("/all_course_actives")
def get_cursor_actives(db: Session = Depends(get_db)):
    try:
        query_all = db.query(Courses).filter(Courses.is_active == 1).all()
        return query_all
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app_cursos.get("/all_course")
def get_cursor_all(db: Session = Depends(get_db)):
    try:
        query_all = db.query(Courses).all()
        return query_all
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app_cursos.delete("/delete_course/{id}")
async def delete_course(id: int, db: Session = Depends(get_db)):
    try:
        delete = db.query(Courses).filter(Courses.id == id).first()
        if delete is None:
            return HTTPException(status_code=404, detail="Not found")
        else:
            db.delete(delete)
            db.commit()
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Error: {e}")

@app_cursos.post("/new_course")
async def crear_curso(
    img_name: UploadFile, name: str = Form(...), 
    price: str = Form(...), description: str = Form(...), 
    is_active: bool = Form(...), db: Session = Depends(get_db)):
    
    with open(os.getcwd() + "/src/images/" + img_name.filename, "wb") as file_data:
        content = await img_name.read()
        file_data.write(content)
        file_data.close()
    try:
        insert = Courses(
            name = name,
            description= description,
            price = price,
            img_name = img_name.filename,
            is_active = is_active
        )
        db.add(insert)
        db.commit()
        db.refresh(insert)
        return insert
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app_cursos.get("/images/{file_name}")
def url_image(file_name: str):
    return FileResponse(os.getcwd() + "/src/images/" + file_name)