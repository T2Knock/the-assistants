from typing import Union
from fastapi import APIRouter
from schemas.item import Item


router = APIRouter(prefix="/items", tags=["items"])


@router.get("/")
def read_item():
    return [{"id": 1, "name": "Item One"}, {"id": 2, "name": "Item Two"}]


@router.get("/{item_id}")
def detail_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@router.put("/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_price": item.price, "item_id": item_id}
