from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import JSONResponse
# none 매개변수에 대한 타입을 명시하기 위해 Optional사용

app = FastAPI()

class Item(BaseModel):
  name: str
  price: float
  is_offer: Optional[bool] = None

@app.get("/items/{item_id}", "TEXT 테스트")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q":q}

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
  return {"item_name": item.name, "item_id": item_id}






@app.post("/register")
async def register_item(item: Item):
    dicted_item = dict(item)
    dicted_item['success'] = True

    return JSONResponse(dicted_item)