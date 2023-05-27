from fastapi import APIRouter

from models.produto import Produto

router = APIRouter()

banco_de_dados = []

@router.post("/")
def add_item(item: Produto):
    banco_de_dados.append(item)
    return Produto

@router.get("/")
def list_item():
    return banco_de_dados