import pygame


class Gameloop:
    def __init__(self, level, renderer, clock):
        self.level = level
        self.renderer = renderer
        self.clock = clock
        self.game_active = True

    def start(self):
        if self.game_active:
            while True:
                if self._handle_events() is False:
                    break
                self.player = self.level.player_sprite

                self._handle_events()
                self.get_input()
                self.level.run()

                self._render()
                self.clock.tick(60)

                if self.level.lives <= 0:
                    self.game_active == False

        else:
            while True:
                if self._handle_events() is False:
                    break
                self._handle_events()
                self.game_over()

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.player.direction.x = 1

        elif keys[pygame.K_LEFT]:
            self.player.direction.x = -1
        else:
            self.player.direction.x = 0

        if keys[pygame.K_SPACE] and self.player.on_floor:
            self.jump(self.player)

        if keys[pygame.K_UP] and self.player.on_floor:
            self.superjump(self.player)

    def jump(self, sprite):
        jump_speed = -20
        sprite.direction.y = jump_speed

    def superjump(self, sprite):
        jump_speed = -30
        sprite.direction.y = jump_speed

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

    def _render(self):
        self.renderer.render()

    def game_over(self):
        self.renderer.end_screen()
