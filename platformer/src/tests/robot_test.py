import pygame
import unittest
from sprites.robot import Robot


class TestPlayer(unittest.TestCase):
    def setUp(self):
        testgroup = pygame.sprite.Group()
        self.robot = Robot((0, 0), [testgroup])

    def test_robot_created_properly(self):
        self.assertNotEqual(self.robot, None)
