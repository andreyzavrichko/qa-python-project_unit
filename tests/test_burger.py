from unittest.mock import MagicMock

import pytest

from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture
def mock_bun():
    bun = MagicMock()
    bun.get_name.return_value = "black bun"
    bun.get_price.return_value = 100.0
    return bun


@pytest.fixture
def mock_sauce():
    ing = MagicMock()
    ing.get_name.return_value = "hot sauce"
    ing.get_type.return_value = INGREDIENT_TYPE_SAUCE
    ing.get_price.return_value = 100.0
    return ing


@pytest.fixture
def mock_filling():
    ing = MagicMock()
    ing.get_name.return_value = "cutlet"
    ing.get_type.return_value = INGREDIENT_TYPE_FILLING
    ing.get_price.return_value = 200.0
    return ing


@pytest.fixture
def burger_with_bun(mock_bun):
    burger = Burger()
    burger.set_buns(mock_bun)
    return burger


def test_set_buns(mock_bun):
    burger = Burger()
    burger.set_buns(mock_bun)
    assert burger.bun is mock_bun


def test_add_ingredient(burger_with_bun, mock_sauce):
    burger_with_bun.add_ingredient(mock_sauce)
    assert mock_sauce in burger_with_bun.ingredients


def test_add_multiple_ingredients(burger_with_bun, mock_sauce, mock_filling):
    burger_with_bun.add_ingredient(mock_sauce)
    burger_with_bun.add_ingredient(mock_filling)
    assert len(burger_with_bun.ingredients) == 2


def test_remove_ingredient(burger_with_bun, mock_sauce, mock_filling):
    burger_with_bun.add_ingredient(mock_sauce)
    burger_with_bun.add_ingredient(mock_filling)
    burger_with_bun.remove_ingredient(0)
    assert mock_sauce not in burger_with_bun.ingredients
    assert len(burger_with_bun.ingredients) == 1


def test_move_ingredient(burger_with_bun, mock_sauce, mock_filling):
    burger_with_bun.add_ingredient(mock_sauce)  # index 0
    burger_with_bun.add_ingredient(mock_filling)  # index 1
    burger_with_bun.move_ingredient(0, 1)
    assert burger_with_bun.ingredients[0] is mock_filling
    assert burger_with_bun.ingredients[1] is mock_sauce


def test_get_price_bun_only(mock_bun):
    burger = Burger()
    burger.set_buns(mock_bun)
    assert burger.get_price() == 200.0


def test_get_price_with_ingredients(burger_with_bun, mock_sauce, mock_filling):
    burger_with_bun.add_ingredient(mock_sauce)
    burger_with_bun.add_ingredient(mock_filling)
    assert burger_with_bun.get_price() == 500.0


def test_get_price_calls_bun_get_price(mock_bun):
    burger = Burger()
    burger.set_buns(mock_bun)
    burger.get_price()
    mock_bun.get_price.assert_called()


def test_get_price_calls_ingredient_get_price(burger_with_bun, mock_sauce):
    burger_with_bun.add_ingredient(mock_sauce)
    burger_with_bun.get_price()
    mock_sauce.get_price.assert_called()


def test_get_receipt_not_none(burger_with_bun, mock_sauce):
    burger_with_bun.add_ingredient(mock_sauce)
    assert burger_with_bun.get_receipt() is not None


def test_get_receipt_contains_bun_name(burger_with_bun):
    receipt = burger_with_bun.get_receipt()
    assert "black bun" in receipt


def test_get_receipt_contains_price(burger_with_bun):
    receipt = burger_with_bun.get_receipt()
    assert "Price:" in receipt


def test_get_receipt_contains_ingredient_name(burger_with_bun, mock_sauce):
    burger_with_bun.add_ingredient(mock_sauce)
    receipt = burger_with_bun.get_receipt()
    assert "hot sauce" in receipt


def test_get_receipt_contains_ingredient_type(burger_with_bun, mock_sauce):
    burger_with_bun.add_ingredient(mock_sauce)
    receipt = burger_with_bun.get_receipt()
    assert INGREDIENT_TYPE_SAUCE.lower() in receipt
