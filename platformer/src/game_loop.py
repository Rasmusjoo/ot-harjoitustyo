import pygame
from support import save_score


class Gameloop:
    def __init__(self, level, renderer, clock, event_queue):
        '''Classes constructor

        Args:
            level: Level class object used in the game
            renderer: Renderer class object
            clock: Clock for the game. Normally pygame.time.Clock()
            event_queue: list of events for the game
        '''
        self.level = level
        self.renderer = renderer
        self.clock = clock
        self.game_state = 0
        self.event_queue = event_queue
        self.player = None

    def start(self):
        '''The core of the gameloop. Handles the gamestates
        '''
        while True:
            if self.handle_events() is False:
                break
            if self.level.level_complete is True:
                self.game_state = 4
            if self.game_state == 0:
                self.handle_events()
                self.renderer.intro_screen()

            elif self.game_state == 1:
                self.player = self.level.player

                self.handle_events()
                self.get_input()
                self.level.run()
                self.renderer.render()

            elif self.game_state == 2:
                self.handle_events()
                self.renderer.pause_screen()

            elif self.game_state == 4:
                self.handle_events()
                self.renderer.victory()

            else:
                self.handle_events()
                self.renderer.end_screen()

            self.clock.tick(60)

    def restart(self):
        '''Resets the game. Returns everything to the state it was in the beginning
        '''
        for sprite in self.level.visible_sprites:
            sprite.kill()
        self.level.level_complete = False
        self.level.points = 0
        self.level.lives = 3
        self.level.setup_level(self.level.level_data)
        self.game_state = 1

    def get_input(self, keys=None):
        '''Takes the movement commands of the user and moves the player accordingly.
        '''
        if not keys:
            keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.player.direction.x = 1
            self.player.orientation = "right"

        elif keys[pygame.K_LEFT]:
            self.player.direction.x = -1
            self.player.orientation = "left"
        else:
            self.player.direction.x = 0

        if keys[pygame.K_SPACE] and self.player.on_floor:
            self.jump(self.player, -20)

        if keys[pygame.K_UP] and self.player.on_floor:
            self.jump(self.player, -30)

    def jump(self, sprite, jump_height):
        '''Moves the sprite up

        Args:
            sprite: The sprite doing the jumping.
            jump_height: The height of the jump
        '''
        jump_speed = jump_height
        sprite.direction.y = jump_speed

    def handle_events(self):
        '''Handles the events. Commands to change the gamestate and shutting down the program.

        Returns:
            False in the case of pygame.QUIT. Otherwise True.
        '''
        for event in self.event_queue.get():
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
                    save_score(self.level.points)
                    self.game_state = 3
            elif self.game_state == 2:
                # Press P to unpause
                if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                    self.game_state = 1
            if self.game_state == 3:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                    self.restart()
            if self.game_state == 4:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                    self.restart()

        return True
