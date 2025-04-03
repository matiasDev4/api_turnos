from pydantic import BaseModel
from fastapi import UploadFile, Form


class ShiftBase(BaseModel):
    id: int
    date : str


class Courser_schema(BaseModel):
    name: str 
    description: str 
    price: int 
    status: bool 

class userRegister(BaseModel):
    username: str
    email: str
    password: str




