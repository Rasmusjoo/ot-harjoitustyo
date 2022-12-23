import pygame
from pygame import sprite
from support import load_assets


class Player(sprite.Sprite):
    def __init__(self, pos, sprite_groups):
        super().__init__(sprite_groups)

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
        """Loads the images for the player's different poses.

        Returns:
            A list of images for the player's poses.
        """
        filenames = ["player", "adventurer_idle.png", "adventurer_running.png",
                     "adventurer_jump.png", "adventurer_fall.png"]

        assets = load_assets(*filenames)

        return assets

    def get_jump_status(self):
        if self.direction.y < 0:
            return "jump"
        return None

    def get_fall_status(self):
        if self.direction.y > 1:
            return "fall"
        return None

    def get_run_status(self):
        if self.direction.x != 0:
            return "run"
        return None

    def get_idle_status(self):
        if self.direction.x == 0:
            return "idle"
        return None

    def get_status(self):
        """Determines the player's status based on their movement.

        Returns:
            The player's status.
        """
        status = self.get_jump_status()
        if status:
            return status

        status = self.get_fall_status()
        if status:
            return status

        status = self.get_run_status()
        if status:
            return status

        return self.get_idle_status()

    def animation(self):
        """Updates the player's image based on their status.

        The image is flipped horizontally if the player is facing left.
        """
        # Map the player's status to the corresponding image in the assets list
        status_mapping = {
            "jump": self.assets[2],
            "fall": self.assets[3],
            "run": self.assets[1],
            "idle": self.assets[0]
        }

        # Set the player's image to the corresponding image based on the status
        self.image = status_mapping[self.status]

        # Flip the image horizontally if the player is facing left
        if self.orientation == "left":
            self.image = pygame.transform.flip(self.image, True, False)

    def update(self):
        '''Updates the player by calling functions
        '''
        self.status = self.get_status()
        self.animation()
