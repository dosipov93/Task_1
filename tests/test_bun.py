import pytest
from praktikum.bun import Bun
from data import BUN_PARAMS

class TestBun:

    @pytest.mark.parametrize('name, price', BUN_PARAMS)
    def test_bun_creation(self, name, price):
        bun = Bun(name, price)
        assert bun.name == name
        assert bun.price == price

    def test_get_name(self, bun):
        assert bun.get_name() == 'Test Bun'

    def test_get_price(self, bun):
        assert bun.get_price() == 100