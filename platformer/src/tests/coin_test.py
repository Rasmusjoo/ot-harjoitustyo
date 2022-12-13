import pygame
import unittest
from sprites.coin import Coin


class TestCoin(unittest.TestCase):
    def setUp(self):
        pygame.display.set_mode((100, 100))
        testgroup = pygame.sprite.Group()
        self.coin = Coin((0, 0), [testgroup])

    def test_coin_created_properly(self):
        self.assertNotEqual(self.coin, None)
