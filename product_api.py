from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List

app = FastAPI()

class Product(BaseModel):
    id: int
    name: str
    price: float = Field(..., gt=0)
    stock: int = Field(..., ge=0)

db = {}

@app.post("/products/")
def create_product(product: Product):
    if product.id in db:
        raise HTTPException(status_code=400, detail="Product ID already exists")
    db[product.id] = product
    return product

@app.get("/products/", response_model=List[Product])
def get_products():
    return list(db.values())

@app.get("/products/{product_id}", response_model=Product)
def get_product(product_id: int):
    if product_id not in db:
        raise HTTPException(status_code=404, detail="Product not found")
    return db[product_id]

@app.put("/products/{product_id}")
def update_product(product_id: int, product: Product):
    if product_id not in db:
        raise HTTPException(status_code=404, detail="Product not found")
    
    db[product_id] = product
    return product

@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    if product_id not in db:
        raise HTTPException(status_code=404, detail="Product not found")
    del db[product_id]
    return {"message": "Product deleted successfully"}