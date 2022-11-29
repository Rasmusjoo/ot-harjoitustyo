import unittest
from sprites.robot import Robot


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.robot = Robot((0, 0))

    def test_robot_created_properly(self):
        self.assertNotEqual(self.robot, None)
