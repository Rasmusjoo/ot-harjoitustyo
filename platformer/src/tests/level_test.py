import unittest
from level import Level
from settings import level_map

class TestLevel(unittest.TestCase):
    def setUp(self):
        self.level = Level(level_map)

    def test_level_created_properly(self):
        self.assertNotEqual(self.level, None)