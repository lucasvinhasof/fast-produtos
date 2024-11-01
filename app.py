from fastapi import FastAPI
from models.product import Product

data = [
    Product(id=1, name="TÊnis da Nike", description="Calçados", price=19),
    Product(id=2, name="Camiseta", description="Roupas", price=29),
    Product(id=3, name="Notebook", description="Eletrônicos", price=39),
]

app = FastAPI()

@app.get("/")
def say_hello():
    return {"FastAPI":"Hello"}

@app.get("/api/produtos")
def get_products():
    """
    Retorna todos os produtos
    """
    return data

@app.get("/api/produtos/{id}")
def get_product_by_id(id: int):
    """
    Endpoint que retorna um produto pelo ID
    """
    for product in data:
        if product.id == id:
            return product
        return {"message": "Nenhum produto encontrado com o ID fornecido"}