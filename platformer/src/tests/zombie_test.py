import unittest
from sprites.zombie import Zombie


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.zombie = Zombie((0, 0))

    def test_zombie_created_properly(self):
        self.assertNotEqual(self.zombie, None)
