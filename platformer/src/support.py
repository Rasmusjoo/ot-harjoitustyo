import os
import pygame
dirname = os.path.dirname(__file__)


def load_assets(folder, filename):
    image = pygame.image.load(
        os.path.join(dirname, "assets", folder, filename)
    )
    return image
