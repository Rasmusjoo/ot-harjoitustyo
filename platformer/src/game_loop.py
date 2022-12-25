import pygame
from support import save_score, kill_all_sprites
from level import Level
from ui.renderer import Renderer
from spritetypes import SpriteType
from gamestate import GameState


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
        self.game_state = GameState.INTRO_SCREEN
        self.event_queue = event_queue
        self.player = None
        self.groups = [self.level.sprites[SpriteType.VISIBLE],
                       self.level.sprites[SpriteType.COLLISION],
                       self.level.sprites[SpriteType.ENEMIES],
                       self.level.sprites[SpriteType.COINS],
                       self.level.sprites[SpriteType.STARS],
                       self.level.sprites[SpriteType.COINS],
                       self.level.sprites[SpriteType.ROBOTS]]

    def start(self):
        while True:
            if self.handle_events() is False:
                break
            self.handle_events()
            if self.level.level_complete is True:
                self.game_state = GameState.VICTORY

            # Dictionary to map game states to their corresponding handling methods
            state_handlers = {
                GameState.INTRO_SCREEN: self.handle_intro_screen,
                GameState.GAMEPLAY: self.handle_gameplay,
                GameState.PAUSE_SCREEN: self.handle_pause_screen,
                GameState.VICTORY: self.handle_victory,
                GameState.END_SCREEN: self.handle_end_screen
            }
            handler = state_handlers.get(
                self.game_state, self.handle_end_screen)
            handler()

            self.clock.tick(60)

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
        save_score(self.level.points, level=self.current_level)

    def handle_end_screen(self):
        self.renderer.end_screen()

    def reset_game(self, game_level):
        """Resets the game to its initial state.

        Args:
            game_level: The game level object.

        Returns:
            None
        """

        kill_all_sprites(self.groups)
        game_level.level_complete = False
        game_level.points = 0
        game_level.lives = 3
        self.game_state = GameState.GAMEPLAY
        game_level.setup_level(game_level.level_data)

    def start_next_level(self):
        '''Creates a new level and renderer and removes previous levels sprites
        '''

        kill_all_sprites(self.groups)
        if self.current_level != "test":
            self.current_level += 1
            if self.current_level >= 4:
                self.current_level = "test"
        self.level = Level(self.current_level)
        window = self.renderer.screen
        self.renderer = Renderer(self.level, window)
        self.level.setup_level(self.level.level_data)
        self.game_state = GameState.GAMEPLAY

    def get_input(self, keys=None):
        """Processes input from the player and updates the player's movement.

        Args:
            keys: A list of keys that are currently being pressed. If not
                provided, the keys will be retrieved using pygame.key.get_pressed().

        Returns:
            None
        """
        if keys is None:
            keys = pygame.key.get_pressed()

        # Dictionary mapping keys to player actions
        key_actions = {
            pygame.K_RIGHT: (1, "right"),
            pygame.K_LEFT: (-1, "left"),
            pygame.K_SPACE: self.jump,
            pygame.K_UP: self.jump
        }

        # Update player's direction and orientation based on key presses
        self.player.direction.x = 0
        for key, action in key_actions.items():
            if keys[key]:
                if isinstance(action, tuple):
                    # Update player's direction and orientation
                    self.player.direction.x, self.player.orientation = action
                else:
                    # Call the action function
                    if key == pygame.K_SPACE:
                        action(self.player, -20)
                    elif key == pygame.K_UP:
                        action(self.player, -30)

    def jump(self, sprite, jump_height):
        '''Moves the sprite up

        Args:
            sprite: The sprite doing the jumping.
            jump_height: The height of the jump
        '''
        if sprite.on_floor:
            jump_speed = jump_height
            sprite.direction.y = jump_speed

    def handle_events(self):
        """Processes events in the event queue and updates the game state as necessary."""
        for event in self.event_queue.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.KEYDOWN:
                if self.game_state == GameState.INTRO_SCREEN:
                    self.handle_start_game_event(event)
                elif self.game_state == GameState.GAMEPLAY:
                    self.handle_game_event(event)
                elif self.game_state == GameState.PAUSE_SCREEN:
                    self.handle_pause_event(event)
                elif self.game_state in (GameState.END_SCREEN, GameState.VICTORY):
                    self.handle_end_of_game_event(event)

        return True

    def handle_start_game_event(self, event):
        """Handles a KEYDOWN event in the start game state."""
        if event.key == pygame.K_SPACE:
            self.game_state = GameState.GAMEPLAY

    def handle_game_event(self, event):
        """Handles a KEYDOWN event in the game state."""
        if event.key == pygame.K_p:
            self.game_state = GameState.PAUSE_SCREEN
        elif event.key == pygame.K_q or self.level.lives <= 0:
            save_score(self.level.points, level=self.current_level)
            self.game_state = GameState.END_SCREEN

    def handle_pause_event(self, event):
        """Handles a KEYDOWN event in the pause state."""
        if event.key == pygame.K_p:
            self.game_state = GameState.GAMEPLAY

    def handle_end_of_game_event(self, event):
        """Handles a KEYDOWN event in the game over state."""
        if event.key == pygame.K_s:
            self.reset_game(self.level)
        elif event.key == pygame.K_c:
            self.start_next_level()
