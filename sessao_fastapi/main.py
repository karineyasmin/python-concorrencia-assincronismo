from fastapi import FastAPI
from pydantic import BaseModel


class Produto(BaseModel):
    id: int
    nome: str
    preco: float
    em_oferta: bool = False


app = FastAPI()
produtos = [
    Produto(id=1, nome="Playstation 5", preco=5400.00, em_oferta=True),
    Produto(id=2, nome="Nintendo Wii", preco=999.99, em_oferta=True),
    Produto(id=3, nome="Xbox 360", preco=1500.00, em_oferta=True),
    Produto(id=4, nome="Super Nintendo", preco=250.0, em_oferta=True),
    Produto(id=5, nome="Atari 2000", preco=199.90, em_oferta=True),
]


@app.get("/")
async def index():
    return {"Geek": "University"}


@app.get("/produtos/{id}")
async def buscar_produto(id: int):
    for produto in produtos:
        if produto.id == id:
            return produto
    return None


@app.put("/produtos/{id}")
async def atualizar_produto(id: int, produto: Produto):
    for prod in produtos:
        if prod.id == id:
            prod = produto
            return prod
    return None


# uvicorn main:app --reload
