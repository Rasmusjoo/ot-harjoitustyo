import pygame
from support import load_assets


class Star(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)

        self.image = load_assets("star", "star.png")

        self.rect = self.image.get_rect(topleft=pos)
