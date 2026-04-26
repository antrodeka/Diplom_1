from bun import Bun
from data import bun_name, bun_price


class TestBun:

    def test_get_name_valid_name_return_name(self):
        test_bun = Bun(bun_name, bun_price)
        assert test_bun.get_name() == bun_name

    def test_get_price_valid_price_return_price(self):
        test_bun = Bun(bun_name, bun_price)
        assert test_bun.get_price() == bun_price

