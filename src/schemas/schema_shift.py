from pydantic import BaseModel


class ShiftBase(BaseModel):
    id: int
    date : str


