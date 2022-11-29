import pygame
from sprites.player import Player
from sprites.robot import Robot
from sprites.zombie import Zombie
from sprites.tiles import Tile
from sprites.coin import Coin
from settings import TILE_SIZE, SCREEN_HIGHT, SCREEN_WIDTH


class Level:
    def __init__(self, level_data):

        # level setup
        self.setup_level(level_data)
        self.world_shift_x = 0
        self.world_shift_x_change = 0
        self.starting_pos = (0, 0)
        self.lives = 3
        self.points = 0

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.zombies = pygame.sprite.Group()
        self.robots = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()

        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                pos_x = col_index * TILE_SIZE
                pos_y = row_index * TILE_SIZE

                if cell == "X":
                    tile = Tile((pos_x, pos_y), TILE_SIZE)
                    self.tiles.add(tile)
                if cell == "P":
                    self.starting_pos = (pos_x, pos_y)
                    player_sprite = Player((pos_x, pos_y))
                    self.player.add(player_sprite)
                if cell == "Z":
                    zombie_sprite = Zombie((pos_x, pos_y))
                    self.zombies.add(zombie_sprite)
                    self.enemies.add(zombie_sprite)
                if cell == "R":
                    robot_sprite = Robot((pos_x, pos_y))
                    self.robots.add(robot_sprite)
                    self.enemies.add(robot_sprite)
                if cell == "C":
                    coin_sprite = Coin((pos_x, pos_y))
                    self.coins.add(coin_sprite)

        self.all_sprites.add(
            self.tiles,
            self.player,
            self.zombies,
            self.robots,
            self.coins
        )

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < SCREEN_WIDTH/4 and direction_x < 0:
            self.world_shift_x = 8
            self.world_shift_x_change += 8
            player.speed = 0
        elif player_x > SCREEN_WIDTH - (SCREEN_WIDTH/4) and direction_x > 0:
            self.world_shift_x = -8
            self.world_shift_x_change -= 8
            player.speed = 0
        else:
            self.world_shift_x = 0
            player.speed = 8

    def player_horizontal_movement_collision(self):
        for player in self.player.sprites():
            player.rect.x += player.direction.x * player.speed
            for sprite in self.tiles.sprites():
                if sprite.rect.colliderect(player.rect):
                    if player.direction.x < 0:
                        player.rect.left = sprite.rect.right
                    elif player.direction.x > 0:
                        player.rect.right = sprite.rect.left

    def robot_horizontal_movement_collision(self):
        for robot in self.robots.sprites():
            robot.rect.x += robot.direction.x * robot.speed
            for sprite in self.tiles.sprites():
                if sprite.rect.colliderect(robot.rect):
                    if robot.direction.x < 0:
                        robot.rect.left = sprite.rect.right
                        robot.direction.x = 1
                    elif robot.direction.x > 0:
                        robot.rect.right = sprite.rect.left
                        robot.direction.x = -1

    def apply_gravity(self, sprite):
        sprite.direction.y += sprite.gravity
        sprite.rect.y += sprite.direction.y

    def character_vertical_movement_collisison(self, group):
        for character in group.sprites():
            self.apply_gravity(character)
            for sprite in self.tiles.sprites():
                if sprite.rect.colliderect(character.rect):
                    if character.direction.y > 0:
                        character.rect.bottom = sprite.rect.top
                        character.direction.y = 0
                    elif character.direction.y < 0:
                        character.rect.top = sprite.rect.bottom
                        character.direction.y = 0

    def player_dies(self):
        player = self.player.sprite
        player.kill()
        self.world_shift_x = -self.world_shift_x_change
        self.world_shift_x_change = 0
        self.player.sprite = Player(self.starting_pos)
        self.all_sprites.add(self.player.sprite)
        self.lives -= 1

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

    def player_collects_a_coin(self):
        player = self.player.sprite
        for sprite in self.coins.sprites():
            if sprite.rect.colliderect(player):
                sprite.kill()
                self.points += 1

    def move_sprites_with_world(self, group, x_shift):
        for sprite in group.sprites():
            sprite.rect.x += x_shift

    def run(self):
        # Level tiles
        self.move_sprites_with_world(self.tiles, self.world_shift_x)
        self.scroll_x()

        # Enemy check
        self.player_hits_an_enemy()

        # Coin check
        self.player_collects_a_coin()

        # Player
        self.player_horizontal_movement_collision()
        self.character_vertical_movement_collisison(self.player)
        self.player_falls_too_far()

        # Zombie
        self.move_sprites_with_world(self.zombies, self.world_shift_x)
        self.character_vertical_movement_collisison(self.zombies)

        # Robot
        self.move_sprites_with_world(self.robots, self.world_shift_x)
        self.robot_horizontal_movement_collision()
        self.character_vertical_movement_collisison(self.robots)

        # Coins
        self.move_sprites_with_world(self.coins, self.world_shift_x)
