from random import choice
import pygame
from pygame.math import Vector2 as vector
from support import load_assets
from sprites.tiles import AnimatedTile


class Enemy(AnimatedTile):
    def __init__(self, pos, groups, image, collsion_sprites):
        super().__init__(pos, groups, image)

        self.collsion_sprites = collsion_sprites
        self.direction = pygame.math.Vector2()

    def horizontal_collision_check(self, collisionpoint):
        '''Checks for sprites collision with a collision sprite in a given location.

        Args:
            collisionpoint: point where the collision is checked
        '''
        return [sprite for sprite in self.collsion_sprites
                if sprite.rect.collidepoint(collisionpoint)]

    def horizontal_movement_collsion(self):
        right_gap = self.rect.bottomright + vector(1, 1)
        right_block = self.rect.midright + vector(1, 0)
        left_gap = self.rect.bottomleft + vector(-1, 1)
        left_block = self.rect.midleft + vector(-1, 0)

        floor_sprites = self.horizontal_collision_check(right_gap)
        wall_sprites = self.horizontal_collision_check(right_block)
        if wall_sprites or not floor_sprites:
            self.direction.x *= -1

        floor_sprites = self.horizontal_collision_check(left_gap)
        wall_sprites = self.horizontal_collision_check(left_block)
        if wall_sprites or not floor_sprites:
            self.direction.x *= -1

        speed = 4
        self.rect.x += self.direction.x * speed


class Robot(Enemy):
    def __init__(self, pos, groups, collision_sprites):
        super().__init__(pos, groups, load_assets(
            "robot", "robot.png")[0], collision_sprites)

        # robot movement
        self.direction = pygame.math.Vector2(choice((1, -1)), 0)


class Zombie(Enemy):
    def __init__(self, pos, groups, collision_sprites):
        super().__init__(pos, groups, load_assets(
            "zombie", "zombie.png")[0], collision_sprites)

        # zombie movement
        self.direction = pygame.math.Vector2()


class Plane(Enemy):
    def __init__(self, pos, groups, collision_sprites):
        super().__init__(pos, groups, pygame.transform.rotozoom(
            load_assets("plane", "plane.png")[0], 0, 1.8), collision_sprites)

        # bee movement
        self.direction = pygame.math.Vector2(choice((1, -1)), 0)


class Ghost(Enemy):
    def __init__(self, pos, groups, collision_sprites):
        super().__init__(pos, groups, pygame.transform.rotozoom(
            load_assets("ghost", "ghost.png")[0], 0, 1.8), collision_sprites)

        # ghost movement
        self.direction = pygame.math.Vector2(choice((1, -1)), 0)
