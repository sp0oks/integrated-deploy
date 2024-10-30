from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger

from src.cocktail.controller import CocktailController

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://frontend:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
controller = CocktailController(logger=logger)


@app.get("/")
async def home():
    return {"message": "welcome to the cocktail api"}


@app.get("/cocktail")
async def random():
    return await controller.get_random()


@app.get("/cocktail/{item_id}")
async def single_item(item_id: int):
    result = await controller.get_item(item_id)
    if not result:
        return {}
    return result
