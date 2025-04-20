from typing import List
from fastapi import APIRouter
from .items import router as items_router

__all__ = ["items_router"]

routers: List[APIRouter] = [items_router]
