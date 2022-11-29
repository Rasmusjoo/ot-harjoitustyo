import unittest
from sprites.coin import Coin


class TestCoin(unittest.TestCase):
    def setUp(self):
        self.coin = Coin((0, 0))

    def test_coin_created_properly(self):
        self.assertNotEqual(self.coin, None)