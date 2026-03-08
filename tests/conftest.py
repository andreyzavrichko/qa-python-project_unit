from unittest.mock import MagicMock

import pytest

from praktikum.burger import Burger
from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture
def database():
    return Database()


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