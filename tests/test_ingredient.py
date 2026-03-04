import pytest

from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

INGREDIENT_PARAMS = [
    (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
    (INGREDIENT_TYPE_SAUCE, "sour cream", 200.0),
    (INGREDIENT_TYPE_FILLING, "cutlet", 100),
    (INGREDIENT_TYPE_FILLING, "dinosaur", 0),
]


@pytest.mark.parametrize("ingredient_type, name, price", INGREDIENT_PARAMS)
def test_get_name(ingredient_type, name, price):
    ingredient = Ingredient(ingredient_type, name, price)
    assert ingredient.get_name() == name


@pytest.mark.parametrize("ingredient_type, name, price", INGREDIENT_PARAMS)
def test_get_price(ingredient_type, name, price):
    ingredient = Ingredient(ingredient_type, name, price)
    assert ingredient.get_price() == price


@pytest.mark.parametrize("ingredient_type, name, price", INGREDIENT_PARAMS)
def test_get_type(ingredient_type, name, price):
    ingredient = Ingredient(ingredient_type, name, price)
    assert ingredient.get_type() == ingredient_type
