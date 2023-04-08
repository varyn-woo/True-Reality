import unittest
from mealplan import *
from recipe import *
from pint import UnitRegistry

ureg = UnitRegistry()
Q_ = ureg.Quantity

class TestRecipe(unittest.TestCase):

    def test_creation(self):
        self._recipes = []
        Recipe('test1', 1, 'hello', '', {'onion': 1, 'water' : Q_(10, 'ml')}, ['add onion to water'])
    
    def test_proportions(self): 
        r = Recipe('test2', 2, '', '', {'onion': 2, 'water' : 10 * ureg.liter, 'other': 1 * ureg.gram}, ['scream'])
        halved = r.get_adjusted_ingredients(1)
        self.assertEqual(halved['onion'], 1)
        self.assertEqual(halved['water'], 5 * ureg.liter)
        self.assertEqual(halved['other'], 0.5 * ureg.gram)
    
class TestShoppingList(unittest.TestCase):
    # TODO: write tests to make sure shopping lists are properly generated
    def basic_test(self):
        pass
    
    def test_diff_units(self):
        pass
    
    def test_incompatible_units(self):
        pass
    
    def test_multiple_recipes(self):
        pass

if __name__ == '__main__':
    unittest.main()