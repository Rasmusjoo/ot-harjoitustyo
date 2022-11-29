import pygame

class Gameloop:
    def __init__(self, level, renderer, clock):
        self.level = level
        self.renderer = renderer
        self.clock = clock

    # pygame setup
    def start(self):
        while True:
            if self._handle_events() is False:
                break
            self.player = self.level.player.sprite

            self._handle_events()
            self.get_input()
            self.level.run()

            self._render()
            self.clock.tick(60)

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.player.direction.x = 1

        elif keys[pygame.K_LEFT]:
            self.player.direction.x = -1
        else:
            self.player.direction.x = 0

        if keys[pygame.K_SPACE]:
            self.player.jump()

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

    def _render(self):
        self.renderer.render()
