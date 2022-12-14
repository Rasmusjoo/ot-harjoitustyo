import pygame


class Clock:
    '''Clock for the game
    '''

    def __init__(self):
        '''Classes constructor
        '''
        self._clock = pygame.time.Clock()

    def tick(self, fps):
        '''Sets the games fps
        '''
        self._clock.tick(fps)

    def get_ticks(self):
        '''Counts time from the start of clock

        Returns:
            pygame.time.get_ticks: time since clock was started
        '''
        return pygame.time.get_ticks()
