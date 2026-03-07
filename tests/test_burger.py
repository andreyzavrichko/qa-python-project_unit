from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE


class TestBurger:

    def test_set_buns(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun is mock_bun

    def test_add_ingredient(self, burger_with_bun, mock_sauce):
        burger_with_bun.add_ingredient(mock_sauce)
        assert mock_sauce in burger_with_bun.ingredients

    def test_add_multiple_ingredients(self, burger_with_bun, mock_sauce, mock_filling):
        burger_with_bun.add_ingredient(mock_sauce)
        burger_with_bun.add_ingredient(mock_filling)
        assert len(burger_with_bun.ingredients) == 2

    def test_remove_ingredient(self, burger_with_bun, mock_sauce, mock_filling):
        burger_with_bun.add_ingredient(mock_sauce)
        burger_with_bun.add_ingredient(mock_filling)
        burger_with_bun.remove_ingredient(0)
        assert mock_sauce not in burger_with_bun.ingredients
        assert len(burger_with_bun.ingredients) == 1

    def test_move_ingredient(self, burger_with_bun, mock_sauce, mock_filling):
        burger_with_bun.add_ingredient(mock_sauce)  # index 0
        burger_with_bun.add_ingredient(mock_filling)  # index 1
        burger_with_bun.move_ingredient(0, 1)
        assert burger_with_bun.ingredients[0] is mock_filling
        assert burger_with_bun.ingredients[1] is mock_sauce

    def test_get_price_bun_only(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.get_price() == 200.0

    def test_get_price_with_ingredients(self, burger_with_bun, mock_sauce, mock_filling):
        burger_with_bun.add_ingredient(mock_sauce)
        burger_with_bun.add_ingredient(mock_filling)
        assert burger_with_bun.get_price() == 500.0

    def test_get_price_calls_bun_get_price(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.get_price()
        mock_bun.get_price.assert_called()

    def test_get_price_calls_ingredient_get_price(self, burger_with_bun, mock_sauce):
        burger_with_bun.add_ingredient(mock_sauce)
        burger_with_bun.get_price()
        mock_sauce.get_price.assert_called()

    def test_get_receipt(self, burger_with_bun, mock_sauce):
        burger_with_bun.add_ingredient(mock_sauce)
        receipt = burger_with_bun.get_receipt()
        assert receipt is not None
        assert "black bun" in receipt
        assert INGREDIENT_TYPE_SAUCE.lower() in receipt
        assert "hot sauce" in receipt
        assert "Price:" in receipt
