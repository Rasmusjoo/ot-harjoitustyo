import pygame
import unittest
from event_queue import EventQueue


class TestEventQueue(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.queue = EventQueue()
