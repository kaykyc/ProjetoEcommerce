from pydantic import BaseModel

class Produto (BaseModel):
    cod: int
    descricao:str 
    preco:float
    qnt: int