from pydantic import BaseModel
from fastapi import UploadFile, Form


class ShiftBase(BaseModel):
    id: int
    date : str


class Courser_schema(BaseModel):
    name: str = Form(...)
    description: str = Form(...)
    img_name: str 
    price: int = Form(...)
    is_active: bool = Form(...)



