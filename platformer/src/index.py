import pygame
from settings import SCREEN_HIGHT, SCREEN_WIDTH, level_map
from level import Level
from renderer import Renderer
from game_loop import Gameloop


def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIGHT))
    pygame.display.set_caption("Adventure")

    level = Level(level_map)
    renderer = Renderer(level, screen)
    clock = pygame.time.Clock()

    game_loop = Gameloop(level, renderer, clock)
    pygame.init()
    game_loop.start()


if __name__ == "__main__":
    main()
