import os
import pygame
from pygame import sprite
dirname = os.path.dirname(__file__)


class Robot(sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        self.image = pygame.image.load(
            os.path.join(dirname, "..", "assets", "robot.png")
        )

        self.rect = self.image.get_rect(topleft=pos)
        self.rect.center = pos

        # robot movement
        self.direction = pygame.math.Vector2(2, 0)
        self.direction.x = 1
        self.gravity = 0.8
        self.speed = 4
