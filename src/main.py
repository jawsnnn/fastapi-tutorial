'''
Application file
'''
from typing import Optional

from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


@app.get("/users/me")
async def get_user_me():
    return {
        "user" : "myself"
    }

@app.get("/users/{username}")
async def get_user(username: str):
    return {
        "user": username
    }

@app.post("/items/")
def create_item(item: Item):
    return item