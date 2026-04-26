from bun import Bun
from data import TestData


class TestBun:

    def test_get_name_valid_name_return_name(self):
        test_bun = Bun(TestData.BUNS_DATA[0][0], TestData.BUNS_DATA[0][1])
        assert test_bun.get_name() == TestData.BUNS_DATA[0][0]

    def test_get_price_valid_price_return_price(self):
        test_bun = Bun(TestData.BUNS_DATA[0][0], TestData.BUNS_DATA[0][1])
        assert test_bun.get_price() == TestData.BUNS_DATA[0][1]
