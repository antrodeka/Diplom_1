import pytest
from unittest.mock import Mock

from data import TestData
from ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE
from burger import Burger


@pytest.fixture
def mock_bun():
    bun = Mock()
    bun.get_name.return_value = TestData.BUNS_DATA[0][0]
    bun.get_price.return_value = TestData.BUNS_DATA[0][1]
    return bun

@pytest.fixture
def mock_ingredient():
    ingredient_1 = Mock()
    ingredient_1.get_price.return_value = TestData.INGREDIENTS_DATA[0][2]
    ingredient_1.get_name.return_value = TestData.INGREDIENTS_DATA[0][1]
    ingredient_1.get_type.return_value = INGREDIENT_TYPE_SAUCE

    ingredient_2 = Mock()
    ingredient_2.get_price.return_value = TestData.INGREDIENTS_DATA[4][2]
    ingredient_2.get_name.return_value = TestData.INGREDIENTS_DATA[4][1]
    ingredient_2.get_type.return_value = INGREDIENT_TYPE_FILLING

    return [ingredient_1, ingredient_2]

@pytest.fixture
def burger_with_ing(mock_ingredient):
    burger = Burger()
    for i in mock_ingredient:
        burger.add_ingredient(i)
    return burger
