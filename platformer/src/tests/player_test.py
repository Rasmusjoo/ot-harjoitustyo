import pygame
import unittest
from sprites.player import Player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        testgroup = pygame.sprite.Group()
        self.player = Player((0, 0), [testgroup])

    def test_player_created_properly(self):
        self.assertNotEqual(self.player, None)
