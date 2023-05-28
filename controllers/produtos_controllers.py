from fastapi import APIRouter

from models.produto import Produto

router = APIRouter()

@router.post("/")
async def add_item(item: Produto):
    await item.save()
    return item

@router.get("/")
async def list_item():
    return await Produto.objects.all()