import os
import pygame
from pygame import sprite
dirname = os.path.dirname(__file__)


class Zombie(sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        self.image = pygame.image.load(
            os.path.join(dirname, "..", "assets", "zombie.png")
        )

        self.rect = self.image.get_rect(topleft=pos)
        self.rect.center = pos

        # zombie movement
        self.direction = pygame.math.Vector2(2, 0)
        self.gravity = 0.8

    def update(self, x_shift):
        self.rect.x += x_shift
