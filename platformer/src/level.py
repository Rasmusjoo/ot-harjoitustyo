import pygame
from pygame.math import Vector2 as vector
from spritetypes import SpriteType
from sprites.player import Player
from sprites.tiles import Star, Coin, Cloud, TerrainTile
from sprites.enemies import Robot, Zombie, Plane
from settings import TILE_SIZE, WINDOW_HIGHT
from ui.camera import CameraGroup
from support import load_level


class Level:
    def __init__(self, levelmap=None):
        '''Classes constructor

        Args:
            levelmap: number of the level
        '''

        self.levelmap = levelmap or "test"

        # sprite group setup
        self.sprites = {
            SpriteType.VISIBLE: CameraGroup(),
            SpriteType.ACTIVE: pygame.sprite.Group(),
            SpriteType.COLLISION: pygame.sprite.Group(),
            SpriteType.ROBOTS: pygame.sprite.Group(),
            SpriteType.ENEMIES: pygame.sprite.Group(),
            SpriteType.COINS: pygame.sprite.Group(),
            SpriteType.STARS: pygame.sprite.Group()
        }

        self.player = None

        # level setup
        self.level_data = load_level(self.levelmap)
        self.setup_level(self.level_data)

        self.starting_pos = (0, 0)
        self.lives = 3
        self.points = 0
        self.level_complete = False

    def setup_level(self, layout=None):
        '''Build the level according to the layout

        Args:
            layout: The level data of given level
        '''

        if not layout:
            layout = self.level_data

        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                pos_x = col_index * TILE_SIZE
                pos_y = row_index * TILE_SIZE
                pos = (pos_x, pos_y)

                if cell == "X":
                    self._add_terrain_tile(pos, "ground")
                elif cell == "G":
                    self._add_terrain_tile(pos, "grass")
                elif cell == "W":
                    self._add_cloud(pos)
                elif cell == "P":
                    self._add_player(pos)
                elif cell == "Z":
                    self._add_zombie(pos)
                elif cell == "R":
                    self._add_robot(pos)
                elif cell == "B":
                    self._add_plane(pos)
                elif cell == "C":
                    self._add_coin(pos)
                elif cell == "S":
                    self._add_star(pos)

    def _add_terrain_tile(self, pos, terrain_type):
        TerrainTile(pos, TILE_SIZE, [
                    self.sprites[SpriteType.VISIBLE],
                    self.sprites[SpriteType.COLLISION]], terrain_type)

    def _add_cloud(self, pos):
        Cloud(pos, [self.sprites[SpriteType.VISIBLE],
              self.sprites[SpriteType.COLLISION]])

    def _add_player(self, pos):
        self.starting_pos = pos
        self.player = Player(
            pos, [self.sprites[SpriteType.VISIBLE], self.sprites[SpriteType.ACTIVE]])

    def _add_zombie(self, pos):
        Zombie(pos, [self.sprites[SpriteType.VISIBLE], self.sprites[SpriteType.ACTIVE],
               self.sprites[SpriteType.ENEMIES]])

    def _add_robot(self, pos):
        Robot(pos, [self.sprites[SpriteType.VISIBLE],
              self.sprites[SpriteType.ACTIVE], self.sprites[SpriteType.ENEMIES],
              self.sprites[SpriteType.ROBOTS]])

    def _add_plane(self, pos):
        Plane(pos, [self.sprites[SpriteType.VISIBLE], self.sprites[SpriteType.ACTIVE],
              self.sprites[SpriteType.ENEMIES]])

    def _add_coin(self, pos):
        Coin(pos, [self.sprites[SpriteType.VISIBLE],
             self.sprites[SpriteType.COINS]])

    def _add_star(self, pos):
        Star(pos, [self.sprites[SpriteType.VISIBLE],
             self.sprites[SpriteType.STARS]])

    def player_horizontal_movement_collision(self):
        """Updates the player's position based on its horizontal
        velocity and handles collisions with collision sprites.
        """
        speed = 8
        player = self.player
        player.rect.x += player.direction.x * speed

        for sprite in self.sprites[SpriteType.COLLISION]:
            if sprite.rect.colliderect(player.rect):
                player.rect.x -= player.direction.x * speed

    def horizontal_collision_check(self, collisionpoint):
        '''Checks for sprites collision with a collision sprite in a given location.

        Args:
            collisionpoint: point where the collision is checked
        '''
        return [sprite for sprite in self.sprites[SpriteType.COLLISION]
                if sprite.rect.collidepoint(collisionpoint)]

    def enemy_horizontal_movement_collision(self):
        for enemy in self.sprites[SpriteType.ENEMIES].sprites():
            right_gap = enemy.rect.bottomright + vector(1, 1)
            right_block = enemy.rect.midright + vector(1, 0)
            left_gap = enemy.rect.bottomleft + vector(-1, 1)
            left_block = enemy.rect.midleft + vector(-1, 0)

            floor_sprites = self.horizontal_collision_check(right_gap)
            wall_sprites = self.horizontal_collision_check(right_block)
            if wall_sprites or not floor_sprites:
                enemy.direction.x *= -1

            floor_sprites = self.horizontal_collision_check(left_gap)
            wall_sprites = self.horizontal_collision_check(left_block)
            if wall_sprites or not floor_sprites:
                enemy.direction.x *= -1

            speed = 4
            enemy.rect.x += enemy.direction.x * speed

    def apply_gravity(self, sprite):
        """Applies gravity to the sprite by increasing
        its vertical velocity and updating its position.
        """
        gravity = 0.8
        sprite.direction.y += gravity
        sprite.rect.y += sprite.direction.y

    def player_vertical_movement_collisison(self):
        '''Applys gravity and checks for collision with floor or similiar
        '''
        player = self.player
        self.apply_gravity(player)
        for sprite in self.sprites[SpriteType.COLLISION].sprites():
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

    def handle_player_death(self, game_window_height):
        """Handles the player's death by checking for a collision with an enemy sprite,
        resetting the player's position and attributes, and reducing the player's lives by 1.
        """
        player = self.player
        enemy_collision = pygame.sprite.spritecollide(
            player, self.sprites[SpriteType.ENEMIES], False, pygame.sprite.collide_mask)
        player_falls = player.rect.y > game_window_height
        if enemy_collision or player_falls:
            self.reset_player_position()
            self.lives -= 1

    def reset_player_position(self):
        """Resets the player's position and attributes to their initial values."""
        self.player.rect.x, self.player.rect.y = self.starting_pos
        self.player.velocity = pygame.math.Vector2(0, 0)
        self.player.direction = pygame.math.Vector2(0, 0)

    def handle_player_collecting_item(self, player_character, item_sprites, item_type):
        """Handles the player character collecting an item.

        Args:
            player_character: The player character object.
            item_sprites: A group of sprites representing the items in the game.
            item_type: The type of item being collected (e.g. 'coin', 'star').

        Returns:
            None
        """
        # Check for collision between player character and item sprites
        item_collision = pygame.sprite.spritecollide(
            player_character, item_sprites, True, pygame.sprite.collide_mask)
        if item_collision:
            if item_type == 'coin':
                # Increment player score and destroy the coin sprite
                self.points += 1
            elif item_type == 'star':
                # Mark the level as complete and destroy the star sprite
                self.level_complete = True

    def run(self):
        '''Updates the level. Does the checks.
        '''
        # Coin check
        self.handle_player_collecting_item(
            self.player, self.sprites[SpriteType.COINS], "coin")

        # Star check
        self.handle_player_collecting_item(
            self.player, self.sprites[SpriteType.STARS], "star")

        # Enemies
        self.enemy_horizontal_movement_collision()

        # Player
        self.player_horizontal_movement_collision()
        self.player_vertical_movement_collisison()
        self.handle_player_death(WINDOW_HIGHT)
        self.player.update()


if __name__ == "__main__":
    pass
