import sys
import pygame
from settings import SCREEN_HIGHT, SCREEN_WIDTH, level_map
from level import Level

# pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIGHT))
pygame.display.set_caption("Adventure")
clock = pygame.time.Clock()
level = Level(level_map, screen)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill("blue")
    font = pygame.font.SysFont("Arial", 34)
    points = font.render(f"Points:{level.points}", True, ("Black"))
    lives = font.render(f"Lives:{level.lives}", True, ("Black"))
    screen.blit(points, (0, 10))
    screen.blit(lives, (0, 60))
    level.run()

    pygame.display.update()
    clock.tick(60)
