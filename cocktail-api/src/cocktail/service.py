from http import HTTPStatus

import aiohttp


class CocktailService:
    async def get_random(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                "https://www.thecocktaildb.com/api/json/v1/1/random.php"
            ) as response:
                if response.status == HTTPStatus.OK:
                    result = await response.text()
                    return result
                return f'{{"status": "{response.status}"}}'

    async def get_drink_by_id(self, id: int):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i={id}"
            ) as response:
                if response.status == HTTPStatus.OK:
                    result = await response.text()
                    return result
                return f'{{"status": "{response.status}"}}'
