from recipe import *
from pint import Quantity

class Mealplan:
    def __init__(self, recipes: list[Recipe]):
        self._recipes = recipes
        
    def get_recipes(self):
        return self._recipes
    
    def add_recipe(self, recipe: Recipe):
        self._recipes.append(recipe)
        
    def remove_recipe(self, recipe_name: str):
        for i in range(len(self._recipes)):
            if self._recipes[i].get_title == recipe_name:
                return self._recipes.pop(i)
        return None
    
    def make_shopping_list(self):
        shopping_list = {}
        for recipe in self._recipes:
            for ingredient, amount in recipe.get_ingredients.items():
                if ingredient in shopping_list:
                    shopping_list[ingredient] += amount
                else:
                    shopping_list[ingredient] = amount
        return shopping_list