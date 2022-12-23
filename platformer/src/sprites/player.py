import pygame
from pygame import sprite
from support import load_assets


class Player(sprite.Sprite):
    def __init__(self, pos, sprite_groups, collision_sprites):
        super().__init__(sprite_groups)

        self.assets = self.load_player_assets()
        self.image = self.assets[0]  # idle image
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=pos)
        self.on_floor = False
        self.status = "idle"
        self.orientation = "right"
        self.collision_sprites = collision_sprites

        # player movement
        self.direction = pygame.math.Vector2()

    def load_player_assets(self):
        """Loads the images for the player's different poses.

        Returns:
            A list of images for the player's poses.
        """
        filenames = ["player", "adventurer_idle.png", "adventurer_running.png",
                     "adventurer_jump.png", "adventurer_fall.png"]

        assets = load_assets(*filenames)

        return assets

    def apply_gravity(self):
        """Applies gravity to the sprite by increasing
        its vertical velocity and updating its position.
        """
        gravity = 0.8
        self.direction.y += gravity
        self.rect.y += self.direction.y

    def player_vertical_movement_collision(self):
        '''Applys gravity and checks for collision with floor or similiar
        '''
        self.apply_gravity()
        for collision_sprite in self.collision_sprites.sprites():
            if collision_sprite.rect.colliderect(self.rect):
                if self.direction.y > 0:
                    self.rect.bottom = collision_sprite.rect.top
                    self.direction.y = 0
                    self.on_floor = True
                elif self.direction.y < 0:
                    self.rect.top = collision_sprite.rect.bottom
                    self.direction.y = 0

            if self.on_floor and self.direction.y != 0:
                self.on_floor = False

    def player_horizontal_movement_collision(self):
        """Updates the player's position based on its horizontal
        velocity and handles collisions with collision sprites.
        """
        speed = 8
        self.rect.x += self.direction.x * speed

        for collsion_sprite in self.collision_sprites.sprites():
            if collsion_sprite.rect.colliderect(self.rect):
                self.rect.x -= self.direction.x * speed

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
        # Create a dictionary mapping states to the conditions that should trigger them
        state_conditions = {
            "jump": self.direction.y < 0,
            "fall": self.direction.y > 1,
            "run": self.direction.x != 0,
            "idle": self.direction.x == 0
        }

        # Iterate through the state conditions and return the first state that is True
        for state, condition in state_conditions.items():
            if condition:
                return state

        # Return "idle" as a default if no other states are triggered
        return "idle"

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
        self.player_horizontal_movement_collision()
        self.player_vertical_movement_collision()
        self.status = self.get_status()
        self.animation()
