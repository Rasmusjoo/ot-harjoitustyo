import pygame
from pygame.math import Vector2 as vector
from sprites.player import Player
from sprites.robot import Robot
from sprites.zombie import Zombie
from sprites.tiles import Tile
from sprites.cloud import Cloud
from sprites.coin import Coin
from sprites.star import Star
from settings import TILE_SIZE, WINDOW_HIGHT
from ui.camera import CameraGroup
from support import load_level


class Level:
    def __init__(self, levelmap):
        '''Classes constructor

        Args:
            levelmap: name of the levels file
        '''

        # sprite group setup
        self.visible_sprites = CameraGroup()
        self.active_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()
        self.robots = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.stars = pygame.sprite.Group()

        self.player = None

        # level setup
        level_data = load_level(levelmap)
        self.level_data = level_data
        self.setup_level(self.level_data)

        self.starting_pos = (0, 0)
        self.lives = 3
        self.points = 0
        self.level_complete = False

    def setup_level(self, layout):
        '''Build the level according to the layout

        Args:
            layout: The level data of given level
        '''

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
                    self.player = Player(
                        (pos_x, pos_y), [self.visible_sprites, self.active_sprites])
                if cell == "Z":
                    Zombie((pos_x, pos_y), [
                           self.visible_sprites, self.active_sprites, self.enemies])
                if cell == "R":
                    Robot((pos_x, pos_y), [
                          self.visible_sprites, self.active_sprites, self.enemies, self.robots])
                if cell == "C":
                    Coin((pos_x, pos_y), [self.visible_sprites, self.coins])
                if cell == "S":
                    Star((pos_x, pos_y), [self.visible_sprites, self.stars])

    def player_horizontal_movement_collision(self):
        '''Moves the player horizontally and checks whether something is in their way.
        '''
        speed = 8
        player = self.player
        player.rect.x += player.direction.x * speed
        for sprite in self.collision_sprites.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    def horizontal_collision_check(self, collisionpoint):
        '''Checks for sprites collision with a collision sprite in a given location.

        Args:
            collisionpoint: point where the collision is checked
        '''
        return [sprite for sprite in self.collision_sprites
                if sprite.rect.collidepoint(collisionpoint)]

    def robot_horizontal_movement_collision(self):
        '''Checks for horizontal collisions for robots.
        Robot changes direction when collision would happen.
        '''
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

            speed = 4
            robot.rect.x += robot.direction.x * speed

    def apply_gravity(self, sprite):
        '''Increases the sprites direction.y attribute making it fall
        '''
        gravity = 0.8
        sprite.direction.y += gravity
        sprite.rect.y += sprite.direction.y

    def player_vertical_movement_collisison(self):
        '''Applys gravity and checks for collision with floor or similiar
        '''
        player = self.player
        self.apply_gravity(player)
        for sprite in self.collision_sprites.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_floor = True
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0

            if player.on_floor and player.direction.y != 0:
                player.on_floor = False

    def player_dies(self):
        '''Kills the player sprite and creates another
        '''
        player = self.player
        player.kill()
        self.player = Player(
            self.starting_pos, [self.visible_sprites, self.active_sprites])
        self.lives -= 1

    def player_falls_too_far(self):
        '''Kills the player sprite if it falls too far.
        '''
        player = self.player
        if player.rect.y > WINDOW_HIGHT:
            self.player_dies()

    def player_hits_an_enemy(self):
        '''Kills the player sprite if they collide with an enemy.
        '''
        player = self.player
        enemy_collision = pygame.sprite.spritecollide(
            player, self.enemies, False, pygame.sprite.collide_mask)
        if enemy_collision:
            self.player_dies()

    def player_collects_a_coin(self):
        '''Destroys the coin and adds one point for the player
        if the player collides with a coin.
        '''
        player = self.player
        coin_collision = pygame.sprite.spritecollide(
            player, self.coins, True, pygame.sprite.collide_mask)
        if coin_collision:
            self.points += 1

    def player_collects_a_star(self):
        '''Destroys the star and marks the level as complete
        when the player collides with a star
        '''
        player = self.player
        star_collision = pygame.sprite.spritecollide(
            player, self.stars, True, pygame.sprite.collide_mask)
        if star_collision:
            self.level_complete = True

    def run(self):
        '''Updates the level. Does the checks.
        '''

        self.active_sprites.update()

        # Coin check
        self.player_collects_a_coin()

        # Star check
        self.player_collects_a_star()

        # Enemy check
        self.player_hits_an_enemy()

        # Player
        self.player_horizontal_movement_collision()
        self.player_vertical_movement_collisison()
        self.player.update()
        self.player_falls_too_far()

        # Robot
        self.robot_horizontal_movement_collision()
