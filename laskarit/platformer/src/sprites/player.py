import pygame
import os
from pygame import sprite
dirname = os.path.dirname(__file__)

class Player(sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        self.image = pygame.image.load(
            os.path.join(dirname, "..", "assets", "adventurer.png")
        )

        self.rect = self.image.get_rect(topleft = pos)
        self.direction = pygame.math.Vector2(2,0)
        self.speed = 8

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1

        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

    def update(self):
        self.get_input()
        self.rect.x += self.direction.x * self.speed