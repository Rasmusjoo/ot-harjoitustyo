import pygame
from settings import SCREEN_HIGHT, SCREEN_WIDTH


class Renderer:
    def __init__(self, level, screen):
        self.level = level
        self.screen = screen

    def render(self):
        self.screen.fill("blue")
        font = pygame.font.SysFont("Arial", 34)
        points = font.render(f"Points:{self.level.points}", True, ("Black"))
        lives = font.render(f"Lives:{self.level.lives}", True, ("Black"))
        self.level.visible_sprites.custom_draw(self.level.player_sprite)
        self.screen.blit(points, (0, 10))
        self.screen.blit(lives, (0, 60))

        pygame.display.update()

    def intro_screen(self):
        self.screen.fill("blue")
        font1 = pygame.font.SysFont("Arial", 100)
        font2 = pygame.font.SysFont("Arial", 50)

        game_name = font1.render(
            "Adventure", True, ("Black"))
        game_name_rect = game_name.get_rect(
            center=(SCREEN_WIDTH/2, SCREEN_HIGHT/2))
        starting_instruction = font2.render(
            "Press SPACE to start", True, ("Black"))
        starting_instruction_rect = starting_instruction.get_rect(
            center=(SCREEN_WIDTH/2, SCREEN_HIGHT/2 + 100))
        self.screen.blit(game_name, game_name_rect)
        self.screen.blit(starting_instruction, starting_instruction_rect)

        pygame.display.update()

    def end_screen(self):
        self.screen.fill("red")
        font1 = pygame.font.SysFont("Arial", 100)
        font2 = pygame.font.SysFont("Arial", 50)

        game_over_text = font1.render(
            "GAME OVER", True, ("Black"))
        game_over_text_rect = game_over_text.get_rect(
            center=(SCREEN_WIDTH/2, SCREEN_HIGHT/2))
        points = font2.render(
            f"Points gained:{self.level.points}", True, ("Black"))
        points_rect = points.get_rect(
            center=(SCREEN_WIDTH/2, SCREEN_HIGHT/2 + 100))
        self.screen.blit(game_over_text, game_over_text_rect)
        self.screen.blit(points, points_rect)

        pygame.display.update()

    def pause_screen(self):
        self.screen.fill("yellow")
        font1 = pygame.font.SysFont("Arial", 100)

        paused_text = font1.render(
            "PAUSED", True, ("Black"))
        paused_text_rect = paused_text.get_rect(
            center=(SCREEN_WIDTH/2, SCREEN_HIGHT/2))
        self.screen.blit(paused_text, paused_text_rect)

        pygame.display.update()
