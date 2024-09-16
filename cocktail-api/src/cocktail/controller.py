import json

from src.cocktail.service import CocktailService
from src.cocktail.models import Cocktail


class CocktailController:
    def __init__(self, logger):
        self.service = CocktailService()
        self.logger = logger

    async def get_random(self):
        response = await self.service.get_random()
        obj = json.loads(response)
        if "status" not in obj.keys():
            self.logger.debug(f"obj = {obj}")
            cocktail = Cocktail(obj["drinks"][0])
            return cocktail
        self.logger.error(f"error: {obj}")
        raise Exception(obj)

    async def get_item(self, id: int):
        response = await self.service.get_drink_by_id(id)
        obj = json.loads(response)
        self.logger.debug(f"obj = {obj}")
        if "status" not in obj.keys():
            if not obj.get("drinks"):
                return None
            cocktail = Cocktail(obj["drinks"][0])
            return cocktail
        self.logger.error(f"error: {obj}")
        raise Exception(obj)

    async def get_page(idx: int, limit: int):
        pass
