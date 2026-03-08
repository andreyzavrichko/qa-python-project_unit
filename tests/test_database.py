from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


class TestDatabase:

    def test_available_buns_count(self, database):
        assert len(database.available_buns()) == 3

    def test_available_ingredients_count(self, database):
        assert len(database.available_ingredients()) == 6

    def test_available_buns_returns_list_of_bun(self, database):
        buns = database.available_buns()
        assert all(isinstance(b, Bun) for b in buns)

    def test_available_ingredients_returns_list_of_ingredient(self, database):
        ingredients = database.available_ingredients()
        assert all(isinstance(i, Ingredient) for i in ingredients)

    def test_available_buns_not_empty(self, database):
        assert database.available_buns()

    def test_available_ingredients_not_empty(self, database):
        assert database.available_ingredients()
