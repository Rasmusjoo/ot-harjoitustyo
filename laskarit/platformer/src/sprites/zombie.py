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

        self.width = self.image.get_width()
        self.hight = self.image.get_height()
        self.rect = self.image.get_rect(topleft=pos)
        self.rect.center = pos

        # zombie movement
        self.direction = pygame.math.Vector2(2, 0)
        self.gravity = 0.8

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def update(self, x_shift):
        self.rect.x += x_shift

#zombie = Zombie((0,0))
#print(f"leveys {zombie.width}")
#print(f"korkeus {zombie.hight}")
