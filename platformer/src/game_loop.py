import pygame
from support import save_score, kill_all_sprites
from level import Level
from ui.renderer import Renderer


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
        self.current_level = self.level.levelmap
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
            self.handle_events()
            if self.level.level_complete is True:
                self.game_state = 4
            if self.game_state == 0:
                self.handle_intro_screen()

            elif self.game_state == 1:
                self.handle_gameplay()

            elif self.game_state == 2:
                self.handle_pause_screen()

            elif self.game_state == 4:
                self.handle_victory()

            else:
                self.handle_end_screen()

            self.clock.tick(60)

        if self.game_state == 4:
            save_score(self.level.points)

    def handle_intro_screen(self):
        self.renderer.intro_screen()

    def handle_gameplay(self):
        self.player = self.level.player
        self.get_input()
        self.level.run()
        self.renderer.render()

    def handle_pause_screen(self):
        self.renderer.pause_screen()

    def handle_victory(self):
        self.renderer.victory()
        save_score(self.level.points)

    def handle_end_screen(self):
        self.renderer.end_screen()

    def restart(self):
        '''Resets the game. Returns everything to the state it was in the beginning
        '''
        kill_all_sprites(self.level.visible_sprites)
        self.level.level_complete = False
        self.level.points = 0
        self.level.lives = 3
        self.level.setup_level(self.level.level_data)
        self.game_state = 1

    def reset_game(self, game_level):
        """Resets the game to its initial state.

        Args:
            game_level: The game level object.

        Returns:
            None
        """
        kill_all_sprites(game_level.visible_sprites)
        game_level.level_complete = False
        game_level.player_score = 0
        game_level.lives = 3
        game_level.setup_level(game_level.level_data)
        self.game_state = 1


    def start_next_level(self):
        kill_all_sprites(self.level.visible_sprites)
        self.current_level += 1
        self.level = Level(self.current_level)
        window = self.renderer.screen
        self.renderer = Renderer(self.level, window)
        self.level.setup_level(self.level.level_data)
        self.game_state = 1

    def get_input(self, keys=None):
        '''Takes the movement commands of the user and moves the player accordingly.
        '''
        if not keys:
            keys = pygame.key.get_pressed()

        self.player.direction.x = 0
        if keys[pygame.K_RIGHT]:
            self.player.direction.x = 1
            self.player.orientation = "right"
        elif keys[pygame.K_LEFT]:
            self.player.direction.x = -1
            self.player.orientation = "left"

        if keys[pygame.K_SPACE] and self.player.on_floor:
            self.jump(self.player, -20)
        elif keys[pygame.K_UP] and self.player.on_floor:
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
        for event in self.event_queue.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.KEYDOWN:
                if self.game_state == 0 and event.key == pygame.K_SPACE:
                    self.game_state = 1
                elif self.game_state == 1 and event.key == pygame.K_p:
                    self.game_state = 2
                elif self.game_state == 2 and event.key == pygame.K_p:
                    self.game_state = 1
                elif self.game_state in (3, 4) and event.key == pygame.K_s:
                    self.reset_game(self.level)
                elif self.game_state in (3, 4) and event.key == pygame.K_c:
                    self.start_next_level()
                elif self.level.lives <= 0 or event.key == pygame.K_q:
                    save_score(self.level.points)
                    self.game_state = 3

        return True
