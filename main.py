from typing import Union

from fastapi import FastAPI

from pydantic import BaseModel

class Produto (BaseModel):
    cod: int
    descricao:str 
    preco:float

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World 2"}


@app.get("/items/{item_id}")
def read_item(item_id: int,p: bool , q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post ("/Produto")
def add_item(novo_produto: Produto):
    return novo_produto