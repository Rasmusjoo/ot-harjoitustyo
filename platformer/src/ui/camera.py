import pygame
from settings import camera_borders


class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        '''Classes constructor
        '''
        super().__init__()
        self.display_surface = pygame.display.get_surface()

        # camera
        self.cam_left = camera_borders['left']
        self.cam_top = camera_borders['top']
        self.cam_width = self.display_surface.get_size(
        )[0] - (self.cam_left + camera_borders['right'])
        self.cam_height = self.display_surface.get_size(
        )[1] - (self.cam_top + camera_borders['bottom'])

        self.camera_rect = pygame.Rect(
            self.cam_left, self.cam_top, self.cam_width, self.cam_height)

    def custom_draw(self, player):
        '''Defines a custom draw method to move camera with player
        '''

        # getting the camera position
        if player.rect.left < self.camera_rect.left:
            self.camera_rect.left = player.rect.left
        if player.rect.right > self.camera_rect.right:
            self.camera_rect.right = player.rect.right
        if player.rect.top < self.camera_rect.top:
            self.camera_rect.top = player.rect.top
        if player.rect.bottom > self.camera_rect.bottom:
            self.camera_rect.bottom = player.rect.bottom

        # camera offset
        offset = pygame.math.Vector2(
            self.camera_rect.left - camera_borders['left'],
            self.camera_rect.top - camera_borders['top'])

        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - offset
            self.display_surface.blit(sprite.image, offset_pos)
