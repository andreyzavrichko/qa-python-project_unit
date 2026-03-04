import pytest

from praktikum.bun import Bun

BUN_PARAMS = [
    ("black bun", 100),
    ("white bun", 200.0),
    ("red bun", 0),
    ("", 9999.99),
]


@pytest.mark.parametrize("name, price", BUN_PARAMS)
def test_get_name(name, price):
    bun = Bun(name, price)
    assert bun.get_name() == name


@pytest.mark.parametrize("name, price", BUN_PARAMS)
def test_get_price(name, price):
    bun = Bun(name, price)
    assert bun.get_price() == price
