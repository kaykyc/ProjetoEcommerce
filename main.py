from typing import Optional, Union

from fastapi import Cookie, FastAPI, Header, Response

from pydantic import BaseModel

class Produto (BaseModel):
    cod: int
    descricao:str 
    preco:float

app = FastAPI()


@app.get("/")
def read_root(user_agent: Optional[str] = Header(123)):
    return {"Welcome to your store,"}
    return{"user agente": user_agent}

@app.get("/cookie")
def cookie(response: Response):
    response.set_cookie(key="meucookie", value="135566")
    return {"cookie": True }

@app.get("/get-cookie")
def get_cookie(meucookie: Optional[str] = Cookie(None)):
    return{"Cookie": meucookie}

@app.get("/items/{item_id}")
def read_item(item_id: int,p: bool , q: Optional[str] = None):
    return {"item_id": item_id, "q": q, "p":p}

@app.post ("/Produto")
def add_item(novo_produto: Produto):
    return novo_produto