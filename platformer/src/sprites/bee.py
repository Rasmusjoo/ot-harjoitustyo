from random import choice
import pygame
from pygame import sprite
from support import load_assets


class Bee(sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)

        folder = "bee"
        self.image = load_assets(folder, "bee.png")
        self.image = pygame.transform.rotozoom(self.image, 0, 3)

        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=pos)
        self.on_floor = False

        # bee movement
        self.direction = pygame.math.Vector2(choice((1, -1)), 0)