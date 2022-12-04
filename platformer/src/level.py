import pygame
from pygame.math import Vector2 as vector
from sprites.player import Player
from sprites.robot import Robot
from sprites.zombie import Zombie
from sprites.tiles import Tile
from sprites.cloud import Cloud
from sprites.coin import Coin
from settings import TILE_SIZE, SCREEN_HIGHT
from camera import CameraGroup


class Level:
    def __init__(self, level_data):

        # sprite group setup
        self.visible_sprites = CameraGroup()
        self.active_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()
        self.player = pygame.sprite.Group()
        self.zombies = pygame.sprite.Group()
        self.robots = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()

        # level setup
        self.setup_level(level_data)

        self.starting_pos = (0, 0)
        self.lives = 3
        self.points = 0

    def setup_level(self, layout):

        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                pos_x = col_index * TILE_SIZE
                pos_y = row_index * TILE_SIZE

                if cell == "X":
                    Tile((pos_x, pos_y), TILE_SIZE, [
                         self.visible_sprites, self.collision_sprites])
                if cell == "W":
                    Cloud((pos_x, pos_y), [
                        self.visible_sprites, self.collision_sprites])
                if cell == "P":
                    self.starting_pos = (pos_x, pos_y)
                    self.player_sprite = Player(
                        (pos_x, pos_y), [self.visible_sprites, self.active_sprites, self.player])
                if cell == "Z":
                    Zombie((pos_x, pos_y), [
                           self.visible_sprites, self.active_sprites, self.enemies, self.zombies])
                if cell == "R":
                    Robot((pos_x, pos_y), [
                          self.visible_sprites, self.active_sprites, self.enemies, self.robots])
                if cell == "C":
                    Coin((pos_x, pos_y), [self.visible_sprites, self.coins])

    def player_horizontal_movement_collision(self):
        player = self.player_sprite
        player.rect.x += player.direction.x * player.speed
        for sprite in self.collision_sprites.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    def horizontal_collision_check(self, collisionpoint):
        return [sprite for sprite in self.collision_sprites
                if sprite.rect.collidepoint(collisionpoint)]

    def robot_horizontal_movement_collision(self):
        for robot in self.robots.sprites():
            right_gap = robot.rect.bottomright + vector(1, 1)
            right_block = robot.rect.midright + vector(1, 0)
            left_gap = robot.rect.bottomleft + vector(-1, 1)
            left_block = robot.rect.midleft + vector(-1, 0)

            if robot.direction.x > 0:  # moving right
                # check floor collision
                floor_sprites = self.horizontal_collision_check(right_gap)
                # check wall collision
                wall_sprites = self.horizontal_collision_check(right_block)
                if wall_sprites or not floor_sprites:
                    robot.direction.x *= -1

            if robot.direction.x < 0:  # moving left
                # check floor collision
                floor_sprites = self.horizontal_collision_check(left_gap)
                # check wall collision
                wall_sprites = self.horizontal_collision_check(left_block)
                if wall_sprites or not floor_sprites:
                    robot.direction.x *= -1

            robot.rect.x += robot.direction.x * robot.speed

    def apply_gravity(self, sprite):
        gravity = 0.8
        sprite.direction.y += gravity
        sprite.rect.y += sprite.direction.y

    def character_vertical_movement_collisison(self, group):
        for character in group.sprites():
            self.apply_gravity(character)
            for sprite in self.collision_sprites.sprites():
                if sprite.rect.colliderect(character.rect):
                    if character.direction.y > 0:
                        character.rect.bottom = sprite.rect.top
                        character.direction.y = 0
                        character.on_floor = True
                    elif character.direction.y < 0:
                        character.rect.top = sprite.rect.bottom
                        character.direction.y = 0

                if character.on_floor and character.direction.y != 0:
                    character.on_floor = False

    def player_dies(self):
        player = self.player_sprite
        player.kill()
        self.player_sprite = Player(
            self.starting_pos, [self.visible_sprites, self.active_sprites, self.player])
        self.lives -= 1

    def player_falls_too_far(self):
        player = self.player_sprite
        if player.rect.y > SCREEN_HIGHT:
            self.player_dies()

    def player_hits_an_enemy(self):
        player = self.player_sprite
        enemy_collision = pygame.sprite.spritecollide(
            player, self.enemies, False, pygame.sprite.collide_mask)
        if enemy_collision:
            self.player_dies()

    def player_collects_a_coin(self):
        player = self.player_sprite
        enemy_collision = pygame.sprite.spritecollide(
            player, self.coins, True, pygame.sprite.collide_mask)
        if enemy_collision:
            self.points += 1

    def run(self):

        self.active_sprites.update()

        # Enemy check
        self.player_hits_an_enemy()

        # Coin check
        self.player_collects_a_coin()

        # Player
        self.player_horizontal_movement_collision()
        self.character_vertical_movement_collisison(self.player)
        self.player_falls_too_far()

        # Zombie
        # self.character_vertical_movement_collisison(self.zombies)

        # Robot
        self.robot_horizontal_movement_collision()
        # self.character_vertical_movement_collisison(self.robots)
