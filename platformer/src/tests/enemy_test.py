import pygame
import unittest
from sprites.enemies import Robot, Zombie, Plane


class TestEnemy(unittest.TestCase):
    def setUp(self):
        pygame.display.set_mode((100, 100))
        testgroup = pygame.sprite.Group()
        collision = pygame.sprite.Group()
        self.zombie = Zombie((200, 0), [testgroup], collision)
        self.robot = Robot((300, 0), [testgroup], collision)
        self.bee = Plane((400, 0), [testgroup], collision)

    def test_robot_created_properly(self):
        self.assertNotEqual(self.robot, None)

    def test_zombie_created_properly(self):
        self.assertNotEqual(self.zombie, None)

    def test_plane_created_properly(self):
        self.assertNotEqual(self.bee, None)
