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
        self.level.all_sprites.draw(self.screen)

        pygame.display.update()
