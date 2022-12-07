import pygame
from support import load_assets


class Coin(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        coin_image = load_assets("coin", "coin.png")

        self.image = pygame.transform.rotozoom(coin_image, 0, 0.5)

        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=pos)
