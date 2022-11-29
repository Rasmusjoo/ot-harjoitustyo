import os
import pygame
from pygame import sprite
dirname = os.path.dirname(__file__)


class Player(sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        self.image = pygame.image.load(
            os.path.join(dirname, "..", "assets", "adventurer.png")
        )

        self.rect = self.image.get_rect(topleft=pos)
        self.rect.center = pos

        # player movement
        self.direction = pygame.math.Vector2(2, 0)
        self.speed = 8
        self.gravity = 0.8
        self.jump_speed = -16

    def jump(self):
        self.direction.y = self.jump_speed
