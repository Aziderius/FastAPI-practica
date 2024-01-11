from typing import Union
from pydantic import BaseModel
from datetime import date

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


class User(BaseModel):
    id: int
    name: str
    joined: date