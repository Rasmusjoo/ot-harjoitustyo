import pygame
import unittest
from game_loop import Gameloop
from level import Level
from settings import WINDOW_HIGHT, WINDOW_WIDTH


class StubClock:
    def tick(self, fps):
        pass

    def get_ticks(self):
        return 0


class StubEvent:
    def __init__(self, event_type, key):
        self.type = event_type
        self.key = key


class StubEventQueue:
    def __init__(self, events):
        self._events = events

    def get(self):
        return self._events


class StubRenderer:
    def render(self):
        pass

    def intro_screen(self):
        pass

    def end_screen(self):
        pass

    def pause_screen(self):
        pass


class TestGameloop(unittest.TestCase):
    def setUp(self):
        pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HIGHT))
        self.testrenderer = StubRenderer()
        self.testclock = pygame.time.Clock()

    def test_game_ends_when_lifes_run_out(self):
        events = [
            StubEvent(pygame.KEYDOWN, pygame.K_SPACE),
        ]
        testlevel = Level()
        testlevel.setup_level()
        test_event_queue = StubEventQueue(events)
        testgameloop = Gameloop(
            testlevel, self.testrenderer, self.testclock, test_event_queue)
        testgameloop.level.lives = 0
        testgameloop.handle_events()
        self.assertEqual(testgameloop.game_state, 3)

    def test_change_gamestate_pause(self):
        events = [
            StubEvent(pygame.KEYDOWN, pygame.K_SPACE), StubEvent(
                pygame.KEYDOWN, pygame.K_p)
        ]
        testlevel = Level()
        testlevel.setup_level()
        test_event_queue = StubEventQueue(events)
        testgameloop = Gameloop(
            testlevel, self.testrenderer, self.testclock, test_event_queue)
        testgameloop.handle_events()
        self.assertEqual(testgameloop.game_state, 2)

    def test_change_gamestate_unpause(self):
        events = [
            StubEvent(pygame.KEYDOWN, pygame.K_SPACE), StubEvent(
                pygame.KEYDOWN, pygame.K_p), StubEvent(pygame.KEYDOWN, pygame.K_p)
        ]
        testlevel = Level()
        testlevel.setup_level()
        test_event_queue = StubEventQueue(events)
        testgameloop = Gameloop(
            testlevel, self.testrenderer, self.testclock, test_event_queue)
        testgameloop.handle_events()
        self.assertEqual(testgameloop.game_state, 1)

    def test_change_gamestate_quit(self):
        events = [
            StubEvent(pygame.KEYDOWN, pygame.K_SPACE), StubEvent(
                pygame.KEYDOWN, pygame.K_q)
        ]
        testlevel = Level()
        testlevel.setup_level()
        test_event_queue = StubEventQueue(events)
        testgameloop = Gameloop(
            testlevel, self.testrenderer, self.testclock, test_event_queue)
        testgameloop.handle_events()
        self.assertEqual(testgameloop.game_state, 3)

    def test_exit(self):
        events = [
            StubEvent(pygame.QUIT, pygame.K_0)
        ]
        testlevel = Level()
        testlevel.setup_level()
        test_event_queue = StubEventQueue(events)
        testgameloop = Gameloop(
            testlevel, self.testrenderer, self.testclock, test_event_queue)
        testgameloop.handle_events()
        self.assertEqual(testgameloop.handle_events(), False)
