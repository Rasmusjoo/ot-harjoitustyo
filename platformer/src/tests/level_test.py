import pygame
import unittest
from level import Level
from settings import level_map


class TestLevel(unittest.TestCase):
    def setUp(self):
        pygame.display.set_mode((1280, 700))
        self.level = Level(level_map)

    def test_level_created_properly(self):
        self.assertNotEqual(self.level, None)

    def test_player_loses_a_life_when_dying(self):
        self.level.player_dies()
        self.assertEqual(self.level.lives, 2)

    def test_coin_check(self):
        self.level.player_collects_a_coin()
        self.assertEqual(self.level.points, 0)

    def test_death_check(self):
        self.level.player_hits_an_enemy()
        self.level.player_falls_too_far()
        self.assertEqual(self.level.lives, 3)
