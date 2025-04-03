from fastapi.routing import APIRouter
from fastapi import Depends, Form , HTTPException, UploadFile, File
from fastapi.responses import FileResponse, JSONResponse
from config.database import session
from sqlalchemy.orm import Session
from models.model_database import Courses
from schemas.schema import Courser_schema
from typing import Annotated, Union
from pathlib import Path
import os
import uuid
import shutil
app_cursos = APIRouter()

SAVE_IMAGE = "imageCourse/"
SAVE_VIDEO = "videoCourse/"
SAVE_IMAGE_PROFILE = "profiles/"

os.makedirs(SAVE_IMAGE, exist_ok=True)
os.makedirs(SAVE_VIDEO, exist_ok=True)
os.makedirs(SAVE_IMAGE_PROFILE, exist_ok=True)


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
    
@app_cursos.get("/Course/{id}")
def get_cursor_all(id: int, db: Session = Depends(get_db)):
    try:
        query = db.query(Courses).filter(Courses.id == id).first()
        return query
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app_cursos.delete("/delete_course/{id}")
async def delete_course(id: int, db: Session = Depends(get_db)):
    try:
        delete = db.query(Courses).filter(Courses.id == id).first()
        if delete is None:
            raise HTTPException(status_code=404, detail="Not found")
        else:
            db.delete(delete)
            db.commit()
            db.refresh(delete)
            return JSONResponse(content={"message": "Curso eliminado!"}, status_code=200)
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Error: {e}")

#creamos la funcion para cambiarle el nombre a los archivos
def create_name_file(file: UploadFile = File(...)) -> str:
    #obtenemos la extencion del archivo
    file_extension = file.filename.split(".")[-1]
    #comprobamos el tipo de extencion
    if file_extension == "png" or "jpg" or "jpeg":
        #si es una imagen se guarda en el directorio de imagenes
        #agregamos el nuevo nombre al archivo
        new_file = f"{uuid.uuid4()}.{file_extension}"
        path_image = os.path.join(SAVE_IMAGE, new_file)

        with open(path_image, "wb") as buf:
            shutil.copyfileobj(file.file, buf)
        return new_file
    

def create_name_video(file: UploadFile = File(...)) -> str:
    file_extension = file.filename.split(".")[-1]
    file_video = f"{uuid.uuid4()}.{file_extension}"
    path_video = os.path.join(SAVE_VIDEO, file_video)
    
    with open(path_video, "wb") as buf:
        shutil.copyfileobj(file.file, buf)
    return file_video


@app_cursos.post("/new_course")
async def crear_curso(
                name: str = Form(...), description: str = Form(...), price: int = Form(...),
                status: bool = Form(...), portada: UploadFile = File(...), video: UploadFile = File(...), db: Session = Depends(get_db)):
    
    try:
        insert = Courses(
            name = name,
            description =  description,
            price = price,
            portada = create_name_file(portada),
            video = create_name_video(video),
            is_active = status
        )
        db.add(insert)
        db.commit()
        db.refresh(insert)
        return insert
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app_cursos.get("/images/{file_name}")
def url_image(file_name: str):
    path = os.path.join(os.getcwd(), "imageCourse", file_name)
    return FileResponse(path)


@app_cursos.get("/videos/{file_name}")
def url_video(file_name: str):
    path = os.path.join(os.getcwd(), "videoCourse", file_name)
    return FileResponse(path)

@app_cursos.put("/update_course/{id}")
def updateCourse(id: int, name: str = Form(...), description: str = Form(...), price: int = Form(...),
                status: bool = Form(...), db: Session = Depends(get_db)):
    try:
        query = db.query(Courses).filter(Courses.id == id).first()
        if query is None:
            raise HTTPException(status_code=404, detail="no encontrado!")
        else:
            query.name = name
            query.description = description
            query.price = price
            query.is_active = status
            db.commit()
            db.refresh(query)
            return query
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))