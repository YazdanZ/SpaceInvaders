import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Aliens of the fleet"""

    DIMENSIONS = (60, 60)

    def __init__(self, screen):
        super().__init__()
        self.screen = screen

        self.image = pygame.image.load("images/alien.bmp")
        self.image = pygame.transform.scale(self.image, Alien.DIMENSIONS)
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def draw(self):
        """Draw the alien at its current position"""
        self.screen.blit(self.image, self.rect)
