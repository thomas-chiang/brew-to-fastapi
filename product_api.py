from fastapi import FastAPI, HTTPException
from typing import List, Optional

app = FastAPI()

db = {}  # In-memory database

class Product:
    def __init__(self, id: int, name: str, description: Optional[str], price: float, stock: int):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock

# Create a product
@app.post("/products/")
def create_product(id: int, name: str, description: Optional[str], price: float, stock: int):
    if id in db:
        raise HTTPException(status_code=400, detail="Product ID already exists")
    db[id] = Product(id, name, description, price, stock)
    return db[id].__dict__

# Read all products
@app.get("/products/", response_model=List[dict])
def get_products():
    return [product.__dict__ for product in db.values()]

# Read a single product
@app.get("/products/{product_id}")
def get_product(product_id: int):
    if product_id not in db:
        raise HTTPException(status_code=404, detail="Product not found")
    return db[product_id].__dict__

# Update a product
@app.put("/products/{product_id}")
def update_product(product_id: int, name: str, description: Optional[str], price: float, stock: int):
    if product_id not in db:
        raise HTTPException(status_code=404, detail="Product not found")
    
    db[product_id].name = name
    db[product_id].description = description
    db[product_id].price = price
    db[product_id].stock = stock
    
    return db[product_id].__dict__

# Delete a product
@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    if product_id not in db:
        raise HTTPException(status_code=404, detail="Product not found")
    del db[product_id]
    return {"message": "Product deleted successfully"}
