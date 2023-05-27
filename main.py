from operator import itemgetter
from typing import ItemsView, Optional, Union

from fastapi import Cookie, FastAPI, Header, Response

from pydantic import BaseModel

class Produto (BaseModel):
    cod: int
    descricao:str 
    preco:float
    qnt: int

app = FastAPI()

banco_de_dados = []

@app.post("/item")
def add_item(item: Produto):
    banco_de_dados.append(item)
    return Produto

@app.get("/item")
def list_item():
    return banco_de_dados

