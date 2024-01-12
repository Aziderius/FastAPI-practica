from uuid import uuid4 as uuid
from typing import Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


class Product(BaseModel):
    id: Optional[str] = None
    name: str
    unit: str
    supplier_price: float
    public_price: float
    supplier: str


app = FastAPI()


products = []


@app.get("/")
async def index():
    return {"msg": "Welcome to Products API"}


@app.get("/products")
async def get_product():
    return products


@app.post("/products")
async def create_product(item: Product):
    item.id = str(uuid())
    products.append(item)
    return {"msg": "Product created successfully"}


@app.get("/products/{product_id}")
async def get_product_id(product_id: str):
    result = list(filter(lambda item: item.id == product_id, products))
    
    if len(result):
        return result
    
    raise HTTPException(status_code=404, detail="Product not found")


@app.delete("/products/{product_id}")
async def delete_product_using_id(product_id: str):
    result = list(filter(lambda item: item.id == product_id, products))
    
    if len(result):
        item = result[0]
        products.remove(item)

        return {"msg": "Product Succesfully deleted"}
    
    raise HTTPException(status_code=404, detail="Product not found")


@app.put("/products/{product_id}")
async def update_product(product_id:str, item: Product):
    result = list(filter(lambda item: item.id == product_id, products))
    
    if len(result):
        item_found = result[0]
        item_found.name = item.name
        item_found.unit = item.unit
        item_found.supplier_price = item.supplier_price
        item_found.public_price = item.public_price
        item_found.supplier = item.supplier

        return item_found

    raise HTTPException(status_code=404, detail="Product not found")
