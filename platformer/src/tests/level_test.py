import pygame
import unittest
from level import Level
from settings import WINDOW_WIDTH, WINDOW_HIGHT


class TestLevel(unittest.TestCase):
    def setUp(self):
        pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HIGHT))
        self.level = Level()
        self.level.setup_level(self.level.level_data)

    def test_level_created_properly(self):
        self.assertNotEqual(self.level, None)

    def test_player_exists(self):
        self.assertNotEqual(self.level.player, None)

    def test_player_loses_a_life_when_dying(self):
        self.level.player_dies()
        self.assertEqual(self.level.lives, 2)

    def test_player_respawn(self):
        self.level.player_dies()
        self.assertNotEqual(self.level.player, None)

    def test_coin_check(self):
        self.level.player_collects_a_coin()
        self.assertEqual(self.level.points, 0)

    def test_death_check_fall(self):
        player = self.level.player
        self.level.player_falls_too_far()

        player.rect.y = WINDOW_HIGHT + 100
        self.level.player_falls_too_far()
        self.assertEqual(self.level.lives, 2)

    def test_death_check_enemy(self):
        self.level.player_hits_an_enemy()
        self.assertEqual(self.level.lives, 3)
