import pygame
import sys
from settings import *
from level import Level

# pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIGHT))
clock = pygame.time.Clock()
level = Level(level_map, screen)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit
            sys.exit()

    screen.fill("blue")
    level.run()

    pygame.display.update()
    clock.tick(60)
