import pygame
from pygame.sprite import Sprite

import settings as game_settings


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

    def update(self):
        """Move the alien"""
        self.x += game_settings.ALIEN_SPEED_FACTOR * game_settings.FLEET_DIRECTION
        self.rect.x = self.x

    def check_edge_collision(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
        else:
            return False
