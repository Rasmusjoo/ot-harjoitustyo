from random import choice
import pygame
from pygame import sprite
from support import load_assets


class Robot(sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)

        folder = "robot"
        self.image = load_assets(folder, "robot.png")

        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=pos)
        self.on_floor = False

        # robot movement
        self.direction = pygame.math.Vector2(choice((1, -1)), 0)
