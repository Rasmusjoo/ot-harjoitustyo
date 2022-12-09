import pygame
import unittest
from clock import Clock


class TestTile(unittest.TestCase):
    def setUp(self):
        self.clock = Clock()

    def test_get_ticks_works_properly(self):
        self.assertEqual(self.clock.get_ticks(), pygame.time.get_ticks())
