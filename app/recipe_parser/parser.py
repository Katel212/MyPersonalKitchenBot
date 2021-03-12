import json
from typing import List

import requests
from bs4 import BeautifulSoup

from app.recipe_parser.recipe_models import Recipe, Ingredient, RecipeDetails


class Parser:
    def __init__(self, url: str):
        self.url = url

    def get_recipes(self) -> List[Recipe]:
        page_content = requests.get(self.url).content.decode("utf8")
        soup = BeautifulSoup(page_content, "html.parser")
        results = soup.find_all("div", class_="anonce-cont-side")
        recipes: List[Recipe] = []

        for result in results:
            image_block = result.find("div", class_="anonce-cont-side-photo").contents[0].contents[0]
            info_block = result.find("div", class_="anonce-cont-side-icons")

            name = str(result.contents[0].contents[0])
            src_ = image_block.attrs['src']
            original = image_block.attrs.get('data-original', '')
            recipe_url = f"https://1000.menu{result.contents[0].attrs['href']}"
            calories = info_block.find("div", class_="info info-left").contents[1].strip()
            cooking_time = info_block.find("div", class_="info info-right").contents[1].text.strip()

            if src_.startswith("//"):
                image = f"https:{src_}"
            else:
                image = f"https:{original}"

            recipe = Recipe(name, image, recipe_url, calories, cooking_time)
            recipes.append(recipe)

        return recipes

    async def get_recipe_details(self, recipe: Recipe) -> RecipeDetails:
        page_content = requests.get(recipe.page_url).content.decode("utf8")
        soup = BeautifulSoup(page_content, "html.parser")
        ingredients_blocks = soup.find_all("div", class_="recept-list-left clf ingredient")
        ingredients: List[Ingredient] = []

        for ingredient in ingredients_blocks:
            container = ingredient.find("p", class_="recept-list-left-bold")
            meta = container.meta
            if meta:
                ingredient_content_parts = meta["content"].split(" - ")
                ingr_name = ingredient_content_parts[0]
                ingr_amount = ingredient_content_parts[1].split(" ")[0]
                ingr_unit = " ".join(ingredient_content_parts[1].split(" ")[1:])
            else:
                ingr_name = ingredient.find("a", class_="name").attrs["title"]
                ingr_amount = container.find("span", class_="value").text.strip()
                ingr_unit = container.find("select").find("option").text.strip()
            ingredients.append(Ingredient(ingr_name, ingr_amount, ingr_unit))

        portions = soup.find("span", id="r_kolvo_porcij").text.strip()

        nutrition_table = soup.find("div", id="nutr_cont_table").find("table").find_all("tr")

        weight = nutrition_table[0].text.strip().split("\n").pop()
        calories = nutrition_table[1].text.strip().split("\n").pop()
        protein = nutrition_table[2].text.strip().split("\n").pop().split(":").pop()
        fat = nutrition_table[3].text.strip().split("\n").pop().split(":").pop()
        carbohydrate = nutrition_table[4].text.strip().split("\n").pop().split(":").pop()
        PFC = nutrition_table[5].text.strip().replace("\n", "").replace("\t", "").split(":").pop()

        steps_block = soup.find("section", id="steps")
        steps = None
        if steps_block:
            steps = []
            step_items = steps_block.find_all("li", class_="clf")
            for step_item in step_items:
                steps.append(step_item.find("p", class_="instruction").text.strip())

        instructions_block = soup.find("div", class_="instructions", itemprop="recipeInstructions")
        instructions = None
        if instructions_block:
            instructions = instructions_block.text.strip()

        recipe_details: RecipeDetails = RecipeDetails(recipe.name, recipe.image, portions, weight, recipe.cooking_time, calories, protein, fat,
                                                      carbohydrate, PFC, ingredients, steps, instructions)

        return recipe_details


class ParserHelper:

    def __init__(self, products: List[str]):
        self.products = products

    async def get_product_id_by_name(self, name: str):
        raw_response = requests.get(f"https://1000.menu/ajax.php?go=free/seek_sostav&term={name}")
        response = json.loads(raw_response.content.decode("utf8"))
        product_id = response[0].get("id", 0)
        return product_id

    async def get_search_string(self) -> str:
        product_ids: List[int] = []
        for product in self.products:
            product_ids.append(await self.get_product_id_by_name(product))
        search_url = f"https://1000.menu/cooking/search?ms=1&str={''.join(['&sostav_arr_add[]=' + str(product_id) for product_id in product_ids])}"
        return search_url
