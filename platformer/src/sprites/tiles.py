import pygame
from settings import TILE_COLOR, TILE_SIZE
from support import load_assets


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups, image):
        super().__init__(groups)
        self.image = image
        self.rect = self.image.get_rect(topleft=pos)
        self.mask = pygame.mask.from_surface(self.image)


class StaticTile(Tile):
    def __init__(self, pos, size, groups, surface=None):
        super().__init__(pos, groups, pygame.Surface((size, size)))
        if surface:
            self.image = surface
        else:
            self.image.fill(TILE_COLOR)


class TerrainTile(StaticTile):
    def __init__(self, pos, size, groups, groundtype=None):
        super().__init__(pos, size, groups, load_assets(
            "ground", f"{groundtype}.png")[0])


class Star(StaticTile):
    def __init__(self, pos, groups):
        super().__init__(pos, TILE_SIZE, groups,
                         load_assets("star", "star.png")[0])


class Coin(StaticTile):
    def __init__(self, pos, groups):
        super().__init__(pos, TILE_SIZE, groups, pygame.transform.rotozoom(
            load_assets("coin", "coin.png")[0], 0, 0.5))


class Cloud(StaticTile):
    def __init__(self, pos, groups):
        super().__init__(pos, TILE_SIZE, groups,
                         load_assets("cloud", "cloud.png")[0])


class AnimatedTile(Tile):
    def __init__(self, pos, groups, image):
        super().__init__(pos, groups, image)

        self.mask = pygame.mask.from_surface(self.image)
        self.on_floor = False
