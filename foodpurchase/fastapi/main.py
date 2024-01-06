# foodpurchase/fastapi/main.py
from fastapi import FastAPI, HTTPException, Depends
from fastapi.openapi.models import APIKey
from fastapi.security import OAuth2PasswordBearer
from django.db import models
from purchases.models import FoodItem
from purchases.serializers import FoodItemSerializer

app = FastAPI()

@app.post("/items/", response_model=FoodItemSerializer)
def create_item(item: FoodItemSerializer):
    return item.dict()

@app.get("/items/{item_id}", response_model=FoodItemSerializer)
def read_item(item_id: int):
    return {"item_id": item_id}

@app.put("/items/{item_id}", response_model=FoodItemSerializer)
def update_item(item_id: int, item: FoodItemSerializer):
    return {"item_id": item_id, **item.dict()}

@app.delete("/items/{item_id}", response_model=FoodItemSerializer)
def delete_item(item_id: int):
    return {"item_id": item_id}
