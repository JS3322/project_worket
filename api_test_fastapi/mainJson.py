from datetime import datetime
from typing import Optional
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

class Item(BaseModel):
  title: str
  timestamp: datetime
  description: Optional[str] = None

fake_db = {}   # 가짜 DB
app = FastAPI()

@app.put("/items/{id}")
def update_item(id: str, item: Item):
  json_compatible_item_data = jsonable_encoder(item)
  fake_db[id] = json_compatible_item_data  # 가짜 DB 업데이트 