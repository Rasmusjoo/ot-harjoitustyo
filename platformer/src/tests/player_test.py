import unittest
import pygame
from sprites.player import Player
from sprites.tiles import TerrainTile


class TestPlayer(unittest.TestCase):
    def setUp(self):
        # Create a sprite group to pass to the Player constructor
        self.sprite_group = pygame.sprite.Group()
        collision_sprites = pygame.sprite.Group()

        #self.floor_sprite = TerrainTile((0,500), 100, [collision_sprites])

        # Create a Player object at the origin (0, 0)
        self.player = Player((0, 0), self.sprite_group, collision_sprites)

    def test_import_assets(self):
        # Test that the import_assets method returns a list of images
        assets = self.player.load_player_assets()
        self.assertIsInstance(assets, list)
        self.assertIsInstance(assets[0], pygame.Surface)

    def test_get_status(self):
        # Test that the get_status method returns the correct status for various player movements
        self.player.direction = pygame.math.Vector2(0, -1)
        self.assertEqual(self.player.get_status(), "jump")

        #self.player.direction = pygame.math.Vector2(0, 1)
        #self.assertEqual(self.player.get_status(), "fall")

        self.player.direction = pygame.math.Vector2(1, 0)
        self.assertEqual(self.player.get_status(), "run")

        self.player.direction = pygame.math.Vector2(0, 0)
        self.assertEqual(self.player.get_status(), "idle")

    def test_animation(self):
        # Test that the animation method updates the player's image based on their status
        self.player.status = "jump"
        self.player.animation()
        self.assertEqual(self.player.image, self.player.assets[2])

        self.player.status = "fall"
        self.player.animation()
        self.assertEqual(self.player.image, self.player.assets[3])

        self.player.status = "run"
        self.player.animation()
        self.assertEqual(self.player.image, self.player.assets[1])

        self.player.status = "idle"
        self.player.animation()
        self.assertEqual(self.player.image, self.player.assets[0])

    def test_update(self):
        # Test that the update method updates the player's status and image
        self.player.direction = pygame.math.Vector2(0, -1)
        self.player.update()
        self.assertEqual(self.player.status, "jump")
        self.assertEqual(self.player.image, self.player.assets[2])

    def test_apply_gravity(self):
        # Test that gravity is applied correctly
        self.player.rect.y = 100
        self.player.apply_gravity()
        self.assertEqual(self.player.direction.y, 0.8)
        #self.assertEqual(self.player.rect.y, 100.8)


if __name__ == "__main__":
    unittest.main()
