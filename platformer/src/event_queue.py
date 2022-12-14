import pygame


class EventQueue:
    '''Class for getting events for the game
    '''

    def get(self):
        '''gets the events

        Returns:
            pygame.event.get: list of events
        '''
        return pygame.event.get()
