import pygame
from settings import camera_borders


class CameraGroup(pygame.sprite.Group):
    """A group of sprites that move with the player character and are
    displayed on the screen with an offset based on the camera's position."""

    CAM_LEFT = camera_borders['left']
    CAM_TOP = camera_borders['top']
    CAM_RIGHT = camera_borders['right']
    CAM_BOTTOM = camera_borders['bottom']

    def __init__(self):
        """Classes constructor."""
        super().__init__()
        self.display_surface = pygame.display.get_surface()

        # Camera dimensions
        self.cam_width = self.display_surface.get_size(
        )[0] - (self.CAM_LEFT + self.CAM_RIGHT)
        self.cam_height = self.display_surface.get_size(
        )[1] - (self.CAM_TOP + self.CAM_BOTTOM)
        self.camera_rect = pygame.Rect(
            self.CAM_LEFT, self.CAM_TOP, self.cam_width, self.cam_height)

    def custom_draw(self, player):
        """Move the camera with the player and blit the sprites in the
        group to the display surface with an offset based on the camera's position."""
        # Update the camera position based on the player's position
        if player.rect.left < self.camera_rect.left:
            self.camera_rect.left = player.rect.left
        if player.rect.right > self.camera_rect.right:
            self.camera_rect.right = player.rect.right
        if player.rect.top < self.camera_rect.top:
            self.camera_rect.top = player.rect.top
        if player.rect.bottom > self.camera_rect.bottom:
            self.camera_rect.bottom = player.rect.bottom

        # Calculate the camera offset
        offset = self.calculate_camera_offset()

        # Blit the sprites in the group to the display surface with the camera offset
        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - offset
            self.display_surface.blit(sprite.image, offset_pos)

    def calculate_camera_offset(self):
        """Calculate the offset for the camera based on its position and the camera borders."""
        return pygame.math.Vector2(self.camera_rect.left - self.CAM_LEFT, self.camera_rect.top - self.CAM_TOP)
