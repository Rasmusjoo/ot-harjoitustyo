import os
import pygame
dirname = os.path.dirname(__file__)

class Coin(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.image.load(
            os.path.join(dirname, "..", "assets", "robot.png")
        )
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift