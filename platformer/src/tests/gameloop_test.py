import pygame
import unittest
from game_loop import Gameloop
from level import Level
from renderer import Renderer
from settings import test_level_map


class TestGameloop(unittest.TestCase):
    def setUp(self):
        testscreen = pygame.display.set_mode((1480, 1000))
        self.testlevel = Level(test_level_map)
        testrenderer = Renderer(self.testlevel, testscreen)
        testclock = pygame.time.Clock()
        self.testgameloop = Gameloop(self.testlevel, testrenderer, testclock)

    def game_ends_when_lifes_run_out(self):
        self.testlevel.lives = 0
        self.testgameloop.handle_events()
        self.assertEqual(self.testgameloop.game_state, 3)
