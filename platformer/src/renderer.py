import pygame


class Renderer:
    def __init__(self, level, screen):
        self.level = level
        self.screen = screen

    def render(self):
        self.screen.fill("blue")
        font = pygame.font.SysFont("Arial", 34)
        points = font.render(f"Points:{self.level.points}", True, ("Black"))
        lives = font.render(f"Lives:{self.level.lives}", True, ("Black"))
        self.screen.blit(points, (0, 10))
        self.screen.blit(lives, (0, 60))
        self.level.visible_sprites.custom_draw(self.level.player_sprite)

        pygame.display.update()

    def end_screen(self):
        self.screen.fill("red")
        font = pygame.font.SysFont("Arial", 50)
        points = font.render(
            f"Points gained:{self.level.points}", True, ("Black"))
        self.screen.blit(points, (200, 500))
