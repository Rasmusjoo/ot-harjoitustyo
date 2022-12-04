import os
import pygame
dirname = os.path.dirname(__file__)


class Cloud(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(
            os.path.join(dirname, "..", "assets", "cloud.png"))

        self.rect = self.image.get_rect(topleft=pos)
