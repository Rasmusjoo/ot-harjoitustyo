from random import choice
import pygame
from support import load_assets
from sprites.tiles import AnimatedTile


class Robot(AnimatedTile):
    def __init__(self, pos, groups):
        super().__init__(pos, groups, load_assets("robot", "robot.png"))

        # robot movement
        self.direction = pygame.math.Vector2(choice((1, -1)), 0)


class Zombie(AnimatedTile):
    def __init__(self, pos, groups):
        super().__init__(pos, groups, load_assets("zombie", "zombie.png"))

        # zombie movement
        self.direction = pygame.math.Vector2()


class Plane(AnimatedTile):
    def __init__(self, pos, groups):
        super().__init__(pos, groups, pygame.transform.rotozoom(
            load_assets("plane", "plane.png"), 0, 1.8))

        # bee movement
        self.direction = pygame.math.Vector2(choice((1, -1)), 0)


class Ghost(AnimatedTile):
    def __init__(self, pos, groups):
        super().__init__(pos, groups, pygame.transform.rotozoom(
            load_assets("ghost", "ghost.png"), 0, 1.8))

        # ghost movement
        self.direction = pygame.math.Vector2(choice((1, -1)), 0)
