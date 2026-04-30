from database import Database
from data import TestData


class TestDatabase:

    def test_avialable_buns_returns_expected_buns_name(self):
        test_db = Database()
        available_buns = test_db.available_buns()
        actual_names = [bun.get_name() for bun in available_buns]
        expected_names = []
        for i in range(0, len(TestData.BUNS_DATA)):
            expected_names.append(TestData.BUNS_DATA[i][0])
        assert actual_names == expected_names

    def test__available_ingredients_returns_expected_ingredients_names(self):
        test_db = Database()
        available_ingredients = test_db.available_ingredients()
        actual_names = [
            ingredient.get_name() for ingredient in available_ingredients]
        expected_names = []
        for i in range(0, len(TestData.INGREDIENTS_DATA)):
            expected_names.append(TestData.INGREDIENTS_DATA[i][1])
        assert actual_names == expected_names
