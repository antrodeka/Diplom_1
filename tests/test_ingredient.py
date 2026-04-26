import pytest

from ingredient import Ingredient
from data import TestData


class TestIngredient:

    @pytest.mark.parametrize('ing_type, name, price',
                             TestData.INGREDIENTS_DATA)
    def test_ingredient_type(self, ing_type, name, price):
        ingredient = Ingredient(ing_type, name, price)
        assert ingredient.get_type() == ing_type

    @pytest.mark.parametrize('ing_type, name, price',
                             TestData.INGREDIENTS_DATA)
    def test_ingredient_price(self, ing_type, name, price):
        ingredient = Ingredient(ing_type, name, price)
        assert ingredient.get_price() == price

    @pytest.mark.parametrize('ing_type, name, price',
                             TestData.INGREDIENTS_DATA)
    def test_ingredient_name(self, ing_type, name, price):
        ingredient = Ingredient(ing_type, name, price)
        assert ingredient.get_name() == name
