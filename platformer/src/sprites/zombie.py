import os
import pygame
from pygame import sprite
dirname = os.path.dirname(__file__)


class Zombie(sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)

        self.image = pygame.image.load(
            os.path.join(dirname, "..", "assets", "zombie.png")
        )

        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=pos)
        self.on_floor = False

        # zombie movement
        self.direction = pygame.math.Vector2()
