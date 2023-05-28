import ormar
from config import database, metadata

class Produto(ormar.Model):
    class Meta:
        metadata = metadata
        database = database

    cod: int = ormar.Integer(primary_key=True)
    nome: str = ormar.String(max_length=50)
    preco: str = ormar.String(max_length=6)
    qnt: int = ormar.Integer(max_value=2)