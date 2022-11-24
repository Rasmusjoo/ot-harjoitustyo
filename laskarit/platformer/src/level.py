import pygame
from sprites.player import Player
from sprites.robot import Robot
from sprites.zombie import Zombie
from sprites.tiles import Tile
from settings import *


class Level:
    def __init__(self, level_data, surface):

        # level setup
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift_x = 0
        self.world_shift_x_change = 0

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.zombie = pygame.sprite.GroupSingle()
        self.robot = pygame.sprite.GroupSingle()
        self.enemies = pygame.sprite.Group()
        self.starting_pos = (0, 0)


        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE

                if cell == "X":
                    tile = Tile((x, y), TILE_SIZE)
                    self.tiles.add(tile)
                if cell == "P":
                    self.starting_pos = (x, y)
                    player_sprite = Player((x, y))
                    self.player.add(player_sprite)
                if cell == "Z":
                    zombie_sprite = Zombie((x, y))
                    self.zombie.add(zombie_sprite)
                    self.enemies.add(zombie_sprite)
                if cell == "R":
                    robot_sprite = Robot((x, y))
                    self.robot.add(robot_sprite)
                    self.enemies.add(robot_sprite)

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < SCREEN_WIDTH/4 and direction_x < 0:
            self.world_shift_x = 8
            self.world_shift_x_change -= 8
            player.speed = 0
        elif player_x > SCREEN_WIDTH - (SCREEN_WIDTH/4) and direction_x > 0:
            self.world_shift_x = -8
            self.world_shift_x_change += 8
            player.speed = 0
        else:
            self.world_shift_x = 0
            player.speed = 8

    def player_horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    def robot_horizontal_movement_collision(self):
        robot = self.robot.sprite
        robot.rect.x += robot.direction.x * robot.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(robot.rect):
                if robot.direction.x < 0:
                    robot.rect.left = sprite.rect.right
                    robot.direction.x = 1
                elif robot.direction.x > 0:
                    robot.rect.right = sprite.rect.left
                    robot.direction.x = -1

    def player_vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0

    def zombie_vertical_movement_collision(self):
        zombie = self.zombie.sprite
        zombie.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(zombie.rect):
                if zombie.direction.y > 0:
                    zombie.rect.bottom = sprite.rect.top
                    zombie.direction.y = 0
                elif zombie.direction.y < 0:
                    zombie.rect.top = sprite.rect.bottom
                    zombie.direction.y = 0

    def robot_vertical_movement_collision(self):
        robot = self.robot.sprite
        robot.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(robot.rect):
                if robot.direction.y > 0:
                    robot.rect.bottom = sprite.rect.top
                    robot.direction.y = 0
                elif robot.direction.y < 0:
                    robot.rect.top = sprite.rect.bottom
                    robot.direction.y = 0

    def player_dies(self):
        player = self.player.sprite
        player.kill()
        self.world_shift_x = self.world_shift_x_change
        self.player.sprite = Player(self.starting_pos)

    def player_falls_too_far(self):
        player = self.player.sprite
        if player.rect.y > SCREEN_HIGHT:
            self.player_dies()

    def player_hits_an_enemy(self):
        player = self.player.sprite
        for sprite in self.enemies.sprites():
            if sprite.rect.colliderect(player):
                self.player_dies()
                return

    def run(self):
        # Level tiles
        self.tiles.update(self.world_shift_x)
        self.tiles.draw(self.display_surface)
        self.scroll_x()

        # Enemy check
        self.player_hits_an_enemy()

        # Player
        self.player.update()
        self.player_horizontal_movement_collision()
        self.player_vertical_movement_collision()
        self.player_falls_too_far()
        self.player.draw(self.display_surface)

        # Zombie
        self.zombie.update(self.world_shift_x)
        self.zombie_vertical_movement_collision()
        self.zombie.draw(self.display_surface)

        # Robot
        self.robot.update(self.world_shift_x)
        self.robot_horizontal_movement_collision()
        self.robot_vertical_movement_collision()
        self.robot.draw(self.display_surface)
         