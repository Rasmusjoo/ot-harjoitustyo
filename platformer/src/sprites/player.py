import pygame
from pygame import sprite
from support import load_assets


class Player(sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)

        self.assets = self.import_assets()

        self.image = self.assets[0]  # idle image
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=pos)
        self.on_floor = False
        self.status = "idle"
        self.orientation = "right"

        # player movement
        self.direction = pygame.math.Vector2()

    def import_assets(self):
        '''Loads the images for players poses
        '''
        folder = "player"

        assets = []

        assets.append(load_assets(folder, "adventurer_idle.png"))
        assets.append(load_assets(folder, "adventurer_running.png"))
        assets.append(load_assets(folder, "adventurer_jump.png"))
        assets.append(load_assets(folder, "adventurer_fall.png"))

        return assets

    def get_status(self):
        '''Sets the status of the player.
        This allows the right pose to be used.
        '''
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
        '''Changes the player pose to match the status.
        '''
        if self.status == "jump":
            self.image = self.assets[2]  # jump image
        elif self.status == "fall":
            self.image = self.assets[3]  # fall image
        elif self.status == "run":
            self.image = self.assets[1]  # run image
        else:
            self.image = self.assets[0]  # idle image

        if self.orientation == "left":
            flipped_image = pygame.transform.flip(self.image, True, False)
            self.image = flipped_image

    def update(self):
        '''Updates the player by calling functions
        '''
        self.get_status()
        self.animation()
