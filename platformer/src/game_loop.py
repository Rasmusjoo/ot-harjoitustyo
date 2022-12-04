import pygame


class Gameloop:
    def __init__(self, level, renderer, clock):
        self.level = level
        self.renderer = renderer
        self.clock = clock
        self.game_state = 0

    def start(self):
        while True:
            if self.handle_events() is False:
                break
            if self.game_state == 0:
                self.handle_events()
                self.intro()

            elif self.game_state == 1:
                self.player = self.level.player_sprite

                self.handle_events()
                self.get_input()
                self.level.run()
                self._render()

            elif self.game_state == 2:
                self.handle_events()
                self.pause()

            else:
                self.handle_events()
                self.game_over()

            self.clock.tick(60)

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

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if self.game_state == 0:
                # Press SPACE to start the game
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.game_state = 1
            if self.game_state == 1:
                # Press P to pause
                if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                    self.game_state = 2
                # game ends when player runs out of lives or presses Q
                q_press = event.type == pygame.KEYDOWN and event.key == pygame.K_q
                if self.level.lives <= 0 or q_press:
                    self.game_state = 3
            elif self.game_state == 2:
                # Press P to unpause
                if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                    self.game_state = 1

        return True

    def _render(self):
        self.renderer.render()

    def intro(self):
        self.renderer.intro_screen()

    def game_over(self):
        self.renderer.end_screen()

    def pause(self):
        self.renderer.pause_screen()
