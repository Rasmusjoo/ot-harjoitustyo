import pygame
from settings import WINDOW_HIGHT, WINDOW_WIDTH
from level import Level
from ui.renderer import Renderer
from game_loop import Gameloop
from event_queue import EventQueue
from clock import Clock


def main():
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HIGHT))
    pygame.display.set_caption("Adventure")

    level = Level("level_normal")
    renderer = Renderer(level, window)
    clock = Clock()
    event_queue = EventQueue()

    game_loop = Gameloop(level, renderer, clock, event_queue)
    pygame.init()
    game_loop.start()


if __name__ == "__main__":
    main()
