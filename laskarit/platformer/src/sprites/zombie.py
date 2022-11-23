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

#zombie = Zombie((0,0))
#print(f"leveys {zombie.width}")
#print(f"korkeus {zombie.hight}")
