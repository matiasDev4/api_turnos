from pydantic import BaseModel


class ShiftBase(BaseModel):
    id: int
    name: str
    date: str
    hour: str
    is_active: bool

