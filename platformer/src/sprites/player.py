import pygame
from support import load_assets
from sprites.tiles import AnimatedTile


class Player(AnimatedTile):
    def __init__(self, pos, sprite_groups, collision_sprites):
        super().__init__(pos, sprite_groups,
                         self.load_player_assets()[0], collision_sprites)

        self.assets = self.load_player_assets()
        self.status = "idle"
        self.orientation = "right"

        self.movement = PlayerMovement(self)
        self.animation = PlayerAnimation(self)

    def load_player_assets(self):
        """Loads the images for the player's different poses.

        Returns:
            A list of images for the player's poses.
        """
        filenames = ["player", "adventurer_idle.png", "adventurer_running.png",
                     "adventurer_jump.png", "adventurer_fall.png"]

        assets = load_assets(*filenames)

        return assets

    def update(self):
        '''Updates the player by calling functions
        '''
        self.movement.player_horizontal_movement_collision()
        self.movement.player_vertical_movement_collision()
        self.status = self.animation.get_status()
        self.animation.animation()


class PlayerMovement:
    def __init__(self, player):
        self.player = player

    def apply_gravity(self):
        """Applies gravity to the player by increasing
        its vertical velocity and updating its position.
        """
        gravity = 0.8
        self.player.direction.y += gravity
        self.player.rect.y += self.player.direction.y

    def player_vertical_movement_collision(self):
        '''Applys gravity and checks for collision with floor or similiar
        '''
        self.apply_gravity()
        for collision_sprite in self.player.collision_sprites.sprites():
            if collision_sprite.rect.colliderect(self.player.rect):
                if self.player.direction.y > 0:
                    self.player.rect.bottom = collision_sprite.rect.top
                    self.player.direction.y = 0
                    self.player.on_floor = True
                elif self.player.direction.y < 0:
                    self.player.rect.top = collision_sprite.rect.bottom
                    self.player.direction.y = 0

            if self.player.on_floor and self.player.direction.y != 0:
                self.player.on_floor = False

    def player_horizontal_movement_collision(self):
        """Updates the player's position based on its horizontal
        velocity and handles collisions with collision sprites.
        """
        speed = 8
        self.player.rect.x += self.player.direction.x * speed

        for collsion_sprite in self.player.collision_sprites.sprites():
            if collsion_sprite.rect.colliderect(self.player.rect):
                self.player.rect.x -= self.player.direction.x * speed


class PlayerAnimation:
    def __init__(self, player):
        self.player = player

    def get_jump_status(self):
        if self.player.direction.y < 0:
            return "jump"
        return None

    def get_fall_status(self):
        if self.player.direction.y > 1:
            return "fall"
        return None

    def get_run_status(self):
        if self.player.direction.x != 0:
            return "run"
        return None

    def get_idle_status(self):
        if self.player.direction.x == 0:
            return "idle"
        return None

    def get_status(self):
        """Determines the player's status based on their movement.

        Returns:
            The player's status.
        """
        # Create a dictionary mapping states to the conditions that should trigger them
        state_conditions = {
            "jump": self.player.direction.y < 0,
            "fall": self.player.direction.y > 1,
            "run": self.player.direction.x != 0,
            "idle": self.player.direction.x == 0
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
            "jump": self.player.assets[2],
            "fall": self.player.assets[3],
            "run": self.player.assets[1],
            "idle": self.player.assets[0]
        }

        # Set the player's image to the corresponding image based on the status
        self.player.image = status_mapping[self.player.status]

        # Flip the image horizontally if the player is facing left
        if self.player.orientation == "left":
            self.player.image = pygame.transform.flip(
                self.player.image, True, False)
