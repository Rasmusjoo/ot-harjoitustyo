import pygame
from settings import WINDOW_HIGHT, WINDOW_WIDTH
from level import Level
from ui.renderer import Renderer
from game_loop import Gameloop
from event_queue import EventQueue
from clock import Clock


def create_window():
    """Creates the game window and sets the caption.

    Returns:
        The game window.
    """
    window_width = WINDOW_WIDTH
    window_height = WINDOW_HIGHT
    window_caption = "Adventure"

    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption(window_caption)

    return window


def create_game_objects(window, level_number=None):
    """Creates the game objects.

    Args:
        window: A window the game is displayed on
        level_number: number of the level to play

    Returns:
        A tuple containing the level, renderer, clock, and event queue.
    """
    if not level_number:
        level_number = "test"
    level = Level(level_number)
    renderer = Renderer(level, window)
    clock = Clock()
    event_queue = EventQueue()

    return level, renderer, clock, event_queue


def run_game_loop(level, renderer, clock, event_queue):
    """Runs the main game loop.
    """
    gameloop = Gameloop(level, renderer, clock, event_queue)
    gameloop.start()


def main():
    """Starts the game.
    """
    pygame.init()
    window = create_window()
    level, renderer, clock, event_queue = create_game_objects(window, 1)
    run_game_loop(level, renderer, clock, event_queue)


if __name__ == "__main__":
    main()
