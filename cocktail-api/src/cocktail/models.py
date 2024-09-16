from dataclasses import dataclass


@dataclass
class Cocktail:
    id: int
    name: str
    img: str
    instructions: str
    ingredients: list

    def __init__(self, obj: dict):
        self.id = int(obj["idDrink"])
        self.name = obj["strDrink"]
        self.img = obj["strDrinkThumb"]
        self.instructions = obj["strInstructions"]
        self.ingredients = []

        i = 0
        while True:
            i += 1
            measure = obj.get(f"strMeasure{i}", "")
            ingredient = obj.get(f"strIngredient{i}")
            if not ingredient:
                break
            self.ingredients.append(f"{measure}{ingredient}")
