from fastapi import FastAPI
from loguru import logger

from src.cocktail.controller import CocktailController

app = FastAPI()
controller = CocktailController(logger=logger)


@app.get("/")
async def home():
    return {"message": "welcome to the cocktail api"}


@app.get("/random")
async def random():
    return await controller.get_random()


@app.get("/items/{page}")
async def item_page(page: int):
    pass


@app.get("/item/{item_id}")
async def single_item(item_id: int):
    result = await controller.get_item(item_id)
    if not result:
        return {}
    return result
