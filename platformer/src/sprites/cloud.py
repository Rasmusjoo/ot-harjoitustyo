import pygame
from support import load_assets


class Cloud(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)

        self.image = load_assets("cloud", "cloud.png")

        self.rect = self.image.get_rect(topleft=pos)
