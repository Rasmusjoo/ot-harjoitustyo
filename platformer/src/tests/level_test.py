import pygame
import unittest
from level import Level
from settings import WINDOW_WIDTH, WINDOW_HIGHT
from spritetypes import SpriteType


class TestLevel(unittest.TestCase):
    def setUp(self):
        pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HIGHT))
        self.level = Level()
        self.level.setup_level(self.level.level_data)
        self.window_height = 700

    def test_level_created_properly(self):
        self.assertNotEqual(self.level, None)

    def test_player_exists(self):
        self.assertNotEqual(self.level.player, None)

    def test_coin_check(self):
        self.level.handle_player_collecting_item(
            self.level.player, self.level.sprites[SpriteType.COINS], "coin")
        self.assertEqual(self.level.points, 0)

    def test_death_check_fall(self):
        player = self.level.player
        self.level.handle_player_death(self.window_height)

        player.rect.y = WINDOW_HIGHT + 100
        self.level.handle_player_death(self.window_height)
        self.assertEqual(self.level.lives, 2)

    def test_death_check_enemy(self):
        self.level.handle_player_death(self.window_height)  # No enemies nearby
        self.assertEqual(self.level.lives, 3)
