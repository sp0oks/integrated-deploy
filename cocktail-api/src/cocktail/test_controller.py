import unittest
import pytest
from loguru import logger

from src.cocktail.controller import CocktailController


class ControllerTest(unittest.IsolatedAsyncioTestCase):
    @pytest.mark.asyncio
    async def test_id_is_valid(self):
        ctrl = CocktailController(logger)
        # pulls a random drink because the cocktaildb does not follow sequential ids
        test_drink = await ctrl.get_random()
        new_drink = await ctrl.get_item(test_drink.id)
        assert new_drink.id == test_drink.id, (
            "error: wrong id obtained when querying specific item"
            f"\nexpected: {test_drink.id}\ngot: {new_drink.id}"
        )

    @unittest.skip
    def test_failure(self):
        raise Exception("test failed")
