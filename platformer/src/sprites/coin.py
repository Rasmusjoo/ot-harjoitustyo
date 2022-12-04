import os
import pygame
dirname = os.path.dirname(__file__)


class Coin(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        coin_image = pygame.image.load(
            os.path.join(dirname, "..", "assets", "coin.png")
        )
        self.image = pygame.transform.rotozoom(coin_image, 0, 0.5)

        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=pos)
