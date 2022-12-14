import pygame
import unittest
from sprites.player import Player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        testgroup = pygame.sprite.Group()
        self.player = Player((0, 0), [testgroup])

    def test_player_created_properly(self):
        self.assertNotEqual(self.player, None)

    def test_player_status_correct(self):
        statuses = []
        correct_statuses = ["jump", "fall", "run", "idle"]

        self.player.direction.y = -10
        self.player.update()
        statuses.append(self.player.status)

        self.player.direction.y = 10
        self.player.update()
        statuses.append(self.player.status)

        self.player.direction.y = 0
        self.player.direction.x = 10
        self.player.update()
        statuses.append(self.player.status)

        self.player.direction.x = 0
        self.player.update()
        statuses.append(self.player.status)

        self.assertEqual(statuses, correct_statuses)
