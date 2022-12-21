import pygame
import unittest
from sprites.tiles import StaticTile, Coin, Star, Cloud


class TestTile(unittest.TestCase):
    def setUp(self):
        testgroup = pygame.sprite.Group()
        self.tile = StaticTile((0, 0), 100, [testgroup])
        self.star = Star((0, 100), [testgroup])
        self.coin = Coin((0, 200), [testgroup])
        self.cloud = Cloud((100, 0), [testgroup])

    def test_tile_created_properly(self):
        self.assertNotEqual(self.tile, None)

    def test_star_created_properly(self):
        self.assertNotEqual(self.star, None)

    def test_coin_created_properly(self):
        self.assertNotEqual(self.coin, None)

    def test_cloud_created_properly(self):
        self.assertNotEqual(self.cloud, None)
