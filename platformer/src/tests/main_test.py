import unittest
import pygame
from level import Level
from ui.renderer import Renderer
from clock import Clock
from event_queue import EventQueue
from index import create_window, create_game_objects
from settings import WINDOW_HIGHT, WINDOW_WIDTH


class TestMain(unittest.TestCase):
    def test_create_window(self):
        # Test that the create_window function creates a window with the correct dimensions and caption
        window = create_window()
        self.assertEqual(window.get_size(), (WINDOW_WIDTH, WINDOW_HIGHT))
        self.assertEqual(pygame.display.get_caption(),
                         ("Adventure", "Adventure"))

    def test_create_game_objects(self):
        # Test that the create_game_objects function creates the correct game objects
        pygame.init()
        window = create_window()
        level, renderer, clock, event_queue = create_game_objects(window)
        self.assertIsInstance(level, Level)
        self.assertIsInstance(renderer, Renderer)
        self.assertIsInstance(clock, Clock)
        self.assertIsInstance(event_queue, EventQueue)


if __name__ == "__main__":
    unittest.main()
