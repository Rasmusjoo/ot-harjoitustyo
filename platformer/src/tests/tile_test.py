import pygame
import unittest
from sprites.tiles import Tile


class TestTile(unittest.TestCase):
    def setUp(self):
        testgroup = pygame.sprite.Group()
        self.tile = Tile((0, 0), 100, [testgroup])

    def test_tile_created_properly(self):
        self.assertNotEqual(self.tile, None)
