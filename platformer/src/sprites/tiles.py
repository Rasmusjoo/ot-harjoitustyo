import pygame
from settings import TILE_COLOR


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size, groups):
        super().__init__(groups)
        self.image = pygame.Surface((size, size))
        self.image.fill(TILE_COLOR)
        self.rect = self.image.get_rect(topleft=pos)
