import unittest
from sprites.player import Player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player((0, 0))

    def test_player_created_properly(self):
        self.assertNotEqual(self.player, None)

    def test_players_speed_is_set_correctly(self):
        self.assertEqual(self.player.speed, 8)
