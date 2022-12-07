import pygame
from pygame import sprite
from support import load_assets


class Player(sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)

        self.assets = self.import_assets()

        self.image = self.assets[0]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=pos)
        self.on_floor = False
        self.status = "idle"
        self.orientation = "right"

        # player movement
        self.direction = pygame.math.Vector2()

    def import_assets(self):
        folder = "player"

        assets = []

        assets.append(load_assets(folder, "adventurer_idle.png"))
        assets.append(load_assets(folder, "adventurer_running.png"))
        assets.append(load_assets(folder, "adventurer_jump.png"))
        assets.append(load_assets(folder, "adventurer_fall.png"))

        return assets

    def get_status(self):
        if self.direction.y < 0:
            self.status = "jump"
        elif self.direction.y > 1:
            self.status = "fall"
        else:
            if self.direction.x != 0:
                self.status = "run"
            else:
                self.status = "idle"

    def animation(self):
        if self.status == "jump":
            self.image = self.assets[2]
        elif self.status == "fall":
            self.image = self.assets[3]
        elif self.status == "run":
            self.image = self.assets[1]
        else:
            self.image = self.assets[0]  # idle

        if self.orientation == "left":
            flipped_image = pygame.transform.flip(self.image, True, False)
            self.image = flipped_image

    def update(self):
        self.get_status()
        self.animation()
