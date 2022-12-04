import pygame
import unittest
from sprites.cloud import Cloud


class TestCloud(unittest.TestCase):
    def setUp(self):
        testgroup = pygame.sprite.Group()
        self.tile = Cloud((0, 0), [testgroup])

    def test_cloud_created_properly(self):
        self.assertNotEqual(self.tile, None)
