import pygame
import unittest
from sprites.zombie import Zombie


class TestPlayer(unittest.TestCase):
    def setUp(self):
        testgroup = pygame.sprite.Group()
        self.zombie = Zombie((0, 0), [testgroup])

    def test_zombie_created_properly(self):
        self.assertNotEqual(self.zombie, None)
