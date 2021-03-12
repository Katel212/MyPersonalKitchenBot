import uuid
from typing import List


class Recipe:
    def __init__(self, name: str, image: str, recipe_url: str, calories: str, cooking_time: str):
        self.id = str(uuid.uuid4().hex)
        self.page_url = recipe_url
        self.name = name
        self.image = image
        self.calories = calories
        self.cooking_time = cooking_time
        self.details = None

    def __repr__(self):
        return f"{self.name}\n\n{self.calories} - {self.cooking_time}"


class Ingredient:
    def __init__(self, name: str, amount: str, unit: str):
        self.name = name
        self.amount = amount
        self.unit = unit

    def __repr__(self):
        return f"{self.name} - {self.amount} {self.unit}"


class RecipeDetails:
    def __init__(self, name: str, image: str, portions_count: int, weight: str, cooking_time: str, calories: str, protein: str, fat: str,
                 carbohydrate: str, PFC: str, ingredients: List[Ingredient], steps: List[str] = None, instructions: str = None, ):
        self.name = name
        self.image = image
        self.portions_count = portions_count
        self.weight = weight
        self.cooking_time = cooking_time
        self.calories = calories
        self.protein = protein
        self.fat = fat
        self.carbohydrate = carbohydrate
        self.PFC = PFC
        self.ingredients = ingredients
        self.steps = steps
        self.instructions = instructions

    def __repr__(self):
        return f"{self.name} ({self.image})\nПорции: {self.portions_count}\nМасса: {self.weight}\nВремя приготовления: {self.cooking_time}\nКалории: {self.calories}\nБелки: {self.protein}\nЖиры: {self.fat}\nУглеводы: {self.carbohydrate}\nБЖУ: {self.PFC}\nИнгредиенты:\n\n{self.ingredients}"
