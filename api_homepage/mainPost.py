from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
# none 매개변수에 대한 타입을 명시하기 위해 Optional사용

app = FastAPI()

class Item(BaseModel):
  name: str
  description: Optional[str] = None
  price: float
  tax: Optional[float] = None

@app.post("/items/")
async def create_item(item: Item):
  # return item          # : string
  item_dict = item.dict()
  if item.tax:
    price_with_tax = item.price + item.tax
    item_dict.update({"price_with_tax": price_with_tax})
  return item_dict