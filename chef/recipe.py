# pint library deals with unit conversions
from pint import Quantity

class Recipe:

    # Initialization
    def __init__(self, title: str, 
                 servings: int, 
                 source: str, 
                 description: str, 
                 ingredients: dict[str, Quantity], 
                 process: list[str]):
        self._title = title
        self._servings = servings
        self._source = source
        self._description = description
        self._ingredients = ingredients
        self._process = process

    # Computational getters
    def get_adjusted_ingredients(self, servings_goal):
        proportion = float(servings_goal) / self._servings
        return {ingredient: amount * proportion for ingredient, amount in self._ingredients.items()}

    # Basic getter methods
    def get_title(self):
        return self._title

    def get_servings(self):
        return self._servings

    def get_source(self):
        return self._source

    def get_description(self):
        return self._description

    def get_ingredients(self):
        return self._ingredients

    def get_process(self):
        return self._process

    # Basic setter methods
    def set_title(self, title):
        self._title = title

    def set_servings(self, servings):
        self._servings = servings

    def set_source(self, source):
        self._source = source

    def set_description(self, description):
        self._description = description

    def set_ingredients(self, ingredients):
        self._ingredients = ingredients

    def set_process(self, process):
        self._process = process
