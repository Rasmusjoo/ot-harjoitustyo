import pygame
from pygame.math import Vector2 as vector
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

        if not levelmap:
            self.levelmap = "test"
        else:
            self.levelmap = levelmap

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
                    self.visible_sprites, self.collision_sprites], terrain_type)

    def _add_cloud(self, pos):
        Cloud(pos, [self.visible_sprites, self.collision_sprites])

    def _add_player(self, pos):
        self.starting_pos = pos
        self.player = Player(pos, [self.visible_sprites, self.active_sprites])

    def _add_zombie(self, pos):
        Zombie(pos, [self.visible_sprites, self.active_sprites, self.enemies])

    def _add_robot(self, pos):
        Robot(pos, [self.visible_sprites,
              self.active_sprites, self.enemies, self.robots])

    def _add_plane(self, pos):
        Plane(pos, [self.visible_sprites, self.active_sprites, self.enemies])

    def _add_coin(self, pos):
        Coin(pos, [self.visible_sprites, self.coins])

    def _add_star(self, pos):
        Star(pos, [self.visible_sprites, self.stars])

    def player_horizontal_movement_collision(self):
        speed = 8
        player = self.player
        player.rect.x += player.direction.x * speed
        for sprite in self.collision_sprites:
            if sprite.rect.colliderect(player.rect):
                player.rect.x -= player.direction.x * speed

    def handle_player_movement_and_collision(self, player_character,
    floor_sprites, collision_sprites):
        """Handles movement and collision detection for the player character.

        Args:
            player_character: The player character object.
            floor_sprites: A group of sprites representing
            the floors or platforms in the game.
            collision_sprites: A group of sprites representing
            the objects that the player character can collide with.

        Returns:
            None
        """
        speed = 8
        # Apply gravity to the player character
        self.apply_gravity(player_character)

        # Move the player character horizontally in
        # the direction specified by their movement direction
        player_character.rect.x += player_character.direction.x * speed

        # Check for collision with floor or platform sprites
        floor_collision = False
        for sprite in floor_sprites.sprites():
            if sprite.rect.colliderect(player_character.rect):
                floor_collision = True
                break
            if floor_collision:
                if player_character.direction.y > 0:
                    # Player is falling and collides with the top of a sprite
                    player_character.rect.bottom = sprite.rect.top
                    player_character.direction.y = 0
                    player_character.on_floor = True
                elif player_character.direction.y < 0:
                    # Player is jumping and collides with the bottom of a sprite
                    player_character.rect.top = sprite.rect.bottom
                    player_character.direction.y = 0
            else:
                player_character.on_floor = False

        # Check for collision with collision sprites
        for sprite in collision_sprites.sprites():
            if sprite.rect.colliderect(player_character.rect):
                # Reverse the horizontal movement if a collision is detected
                player_character.rect.x -= player_character.horizontal_movement_direction * speed

    def horizontal_collision_check(self, collisionpoint):
        '''Checks for sprites collision with a collision sprite in a given location.

        Args:
            collisionpoint: point where the collision is checked
        '''
        return [sprite for sprite in self.collision_sprites
                if sprite.rect.collidepoint(collisionpoint)]

    def enemy_horizontal_movement_collision(self):
        for enemy in self.enemies.sprites():
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

    def handle_player_death(self):
        '''Resets the player and takes away one life
        '''
        # Set the player character's position to the starting position
        self.player.rect.x, self.player.rect.y = self.starting_pos

        # Reset player character attributes
        self.player.velocity = pygame.math.Vector2(0, 0)
        self.player.direction = pygame.math.Vector2(0, 0)
        self.lives -= 1

    def check_for_player_fallen_too_far(self, player_character, game_window_height):
        """Checks if the player character has fallen too far
        and triggers a death event if they have.

        Args:
            player_character: The player character object.
            game_window_height: The height of the game window.

        Returns:
            None
        """
        if player_character.rect.y > game_window_height:
            self.handle_player_death()

    def player_hits_an_enemy(self):
        '''Kills the player sprite if they collide with an enemy.
        '''
        player = self.player
        enemy_collision = pygame.sprite.spritecollide(
            player, self.enemies, False, pygame.sprite.collide_mask)
        if enemy_collision:
            self.handle_player_death()

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

        self.active_sprites.update()

        # Coin check
        self.handle_player_collecting_item(self.player, self.coins, "coin")

        # Star check
        self.handle_player_collecting_item(self.player, self.stars, "star")

        # Enemy check
        self.player_hits_an_enemy()

        # Player
        self.player_horizontal_movement_collision()
        self.player_vertical_movement_collisison()
        self.player.update()
        self.check_for_player_fallen_too_far(self.player, WINDOW_HIGHT)

        # Enemies
        self.enemy_horizontal_movement_collision()
        for enemy in self.enemies:
            enemy.update()


if __name__ == "__main__":
    pass
