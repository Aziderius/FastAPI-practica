from typing import Union
from fastapi import FastAPI
from models.item_models import Item, User

#creación de una aplicación FastAPI
app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/greetings")
async def read_root_2():
    return {"Hola": "Mi-Rey"}


@app.get("/calculator")
async def calculate(operator_1: float, operator_2: float):
    return {"sum": operator_1 + operator_2}


@app.get("/items/{item_id}")
async def read_item(item_id: int, thing: Union[str, None] = None):
    return {"item_id": item_id, "thing": thing}


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id, "item_price": item.price}
