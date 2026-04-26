from burger import Burger


class TestBurger:

    def test_bun_with_valid_bun_sets_bun(self, mock_bun):
        test_burger = Burger()
        test_burger.set_buns(mock_bun)
        assert test_burger.bun == mock_bun

    def test_add_ingredient_with_valid_ing_ing_append_to_list(
            self, mock_ingredient):
        test_burger = Burger()
        for i in mock_ingredient:
            test_burger.add_ingredient(i)
        assert test_burger.ingredients == mock_ingredient

    def test_remove_ingredient_with_valid_ing_ing_removed_from_list(
            self, burger_with_ing, mock_ingredient):
        burger_with_ing.remove_ingredient(0)
        assert burger_with_ing.ingredients[0] == mock_ingredient[1]

    def test_move_ingredient_with_valid_index_ing_moved_in_list(
            self, burger_with_ing, mock_ingredient):
        burger_with_ing.move_ingredient(1, 0)
        assert burger_with_ing.ingredients[0] == mock_ingredient[1]

    def test_get_price_with_bun_and_ing_returns_correct_price(
            self, mock_bun, burger_with_ing, mock_ingredient):
        burger_with_ing.set_buns(mock_bun)
        ing_price = sum(i.get_price.return_value for i in mock_ingredient) 
        expected_price = (mock_bun.get_price.return_value * 2 + ing_price)
        assert burger_with_ing.get_price() == expected_price

    def test_get_receipt_with_bun_and_ing_returns_receipt(
            self, mock_bun, burger_with_ing, mock_ingredient):
        burger_with_ing.set_buns(mock_bun)
        expected_receipt = [f"(==== {mock_bun.get_name()} ====)\n"]
        for i in mock_ingredient:
            expected_receipt.append(
                f"= {i.get_type().lower()} {i.get_name()} =\n")
        expected_receipt.append(f"(==== {mock_bun.get_name()} ====)\n\n")
        expected_receipt.append(f"Price: {burger_with_ing.get_price()}")
        assert burger_with_ing.get_receipt() == ''.join(expected_receipt)
