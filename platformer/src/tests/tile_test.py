import unittest
from sprites.tiles import Tile


class TestTile(unittest.TestCase):
    def setUp(self):
        self.tile = Tile((0, 0), 100)

    def test_tile_created_properly(self):
        self.assertNotEqual(self.tile, None)
