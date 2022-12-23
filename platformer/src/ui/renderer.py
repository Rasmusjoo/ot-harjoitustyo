import pygame
from settings import WINDOW_HIGHT, WINDOW_WIDTH, SKY_COLOR, PAUSE_COLOR, END_COLOR, FONT_COLOR, FONT
from support import fetch_scores
from spritetypes import SpriteType
from support import load_assets


class Renderer:
    '''Class for drawing everything in the game

    Attributes:
        level: Level class object to draw
        screen: Screen to draw on
    '''

    def __init__(self, level, screen):
        '''Classes constructor

        Args:
            level: Level class object to draw
            screen: Screen to draw on
        '''
        self.level = level
        self.screen = screen

    def render(self):
        '''Draws the gameplay
        '''
        self.screen.fill(SKY_COLOR)
        font = pygame.font.SysFont(FONT, 34)
        points = font.render(f"Points:{self.level.points}", True, (FONT_COLOR))
        lives = font.render(f"Lives:{self.level.lives}", True, (FONT_COLOR))
        self.level.sprites[SpriteType.VISIBLE].custom_draw(self.level.player)
        self.screen.blit(points, (0, 10))
        self.screen.blit(lives, (0, 60))

        pygame.display.update()

    def intro_screen(self):
        """Displays the starting screen for the game.

        The screen consists of the game's title, background image, and instructions for starting the game.
        """
        # Load the background image
        background_image = pygame.transform.rotozoom(
            load_assets("backgrounds", "background_2.png")[0], False, 1.5)
        background_rect = background_image.get_rect()

        # Blit the background image to the screen
        self.screen.blit(background_image, background_rect)

        # Define the font and font sizes to use
        font1 = pygame.font.SysFont(FONT, 100)
        font2 = pygame.font.SysFont(FONT, 50)

        # Render the game's title and starting instructions
        try:
            game_name = font1.render("Adventure", True, FONT_COLOR)
            game_name_rect = game_name.get_rect(
                center=(WINDOW_WIDTH / 2, WINDOW_HIGHT / 2))
            starting_instruction = font2.render(
                "Press SPACE to start", True, FONT_COLOR)
            starting_instruction_rect = starting_instruction.get_rect(
                center=(WINDOW_WIDTH / 2, WINDOW_HIGHT / 2 + 100))
        except Exception as e:
            print(f"Unable to render text: {e}")

        # Blit the game's title and starting instructions to the screen
        self.screen.blit(game_name, game_name_rect)
        self.screen.blit(starting_instruction, starting_instruction_rect)

        # Update the display
        pygame.display.update()

    def end_screen(self):
        '''Draws the end screen
        '''
        scores = fetch_scores()
        self.screen.fill(END_COLOR)

        font1 = pygame.font.SysFont(FONT, 150)
        game_over = font1.render("GAME OVER", True, (FONT_COLOR))
        game_over_rect = game_over.get_rect(center=(WINDOW_WIDTH/2, 100))

        font2 = pygame.font.SysFont(FONT, 50)
        points = font2.render(
            f"Points gained:{self.level.points}", True, (FONT_COLOR))
        points_rect = points.get_rect(center=(WINDOW_WIDTH/2, 300))
        score_max = font2.render(
            f"Best score:{max(scores)}", True, (FONT_COLOR))
        score_max_rect = score_max.get_rect(center=(WINDOW_WIDTH/2, 400))

        font3 = pygame.font.SysFont(FONT, 100)
        restart = font3.render("Press S to restart", True, (FONT_COLOR))
        restart_rect = restart.get_rect(
            center=(WINDOW_WIDTH/2, WINDOW_HIGHT/2 + 100))

        self.screen.blit(game_over, game_over_rect)
        self.screen.blit(points, points_rect)
        self.screen.blit(restart, restart_rect)
        self.screen.blit(score_max, score_max_rect)

        pygame.display.update()

    def victory(self):
        '''Draws the victory screen
        '''
        scores = fetch_scores()
        self.screen.fill("green")

        font1 = pygame.font.SysFont(FONT, 150)
        game_over = font1.render("LEVEL COMPLETE", True, (FONT_COLOR))
        game_over_rect = game_over.get_rect(center=(WINDOW_WIDTH/2, 100))

        font2 = pygame.font.SysFont(FONT, 50)
        points = font2.render(
            f"Points gained:{self.level.points}", True, (FONT_COLOR))
        points_rect = points.get_rect(center=(WINDOW_WIDTH/2, 300))
        score_max = font2.render(
            f"Best score:{max(scores)}", True, (FONT_COLOR))
        score_max_rect = score_max.get_rect(center=(WINDOW_WIDTH/2, 400))

        font3 = pygame.font.SysFont(FONT, 100)
        restart = font3.render("Press S to restart", True, (FONT_COLOR))
        restart_rect = restart.get_rect(
            center=(WINDOW_WIDTH/2, WINDOW_HIGHT/2 + 100))

        self.screen.blit(game_over, game_over_rect)
        self.screen.blit(points, points_rect)
        self.screen.blit(restart, restart_rect)
        self.screen.blit(score_max, score_max_rect)

        pygame.display.update()

    def pause_screen(self):
        '''Draws the pause screen
        '''
        self.screen.fill(PAUSE_COLOR)
        font1 = pygame.font.SysFont(FONT, 100)

        paused_text = font1.render(
            "PAUSED", True, (FONT_COLOR))
        paused_text_rect = paused_text.get_rect(
            center=(WINDOW_WIDTH/2, WINDOW_HIGHT/2))
        self.screen.blit(paused_text, paused_text_rect)

        pygame.display.update()
