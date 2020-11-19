import pygame
from pygame.sprite import Sprite

import settings as game_settings


class Bullet(Sprite):
    """Bullet fired from the ship"""

    DIMENSIONS = (game_settings.BULLET_WIDTH, game_settings.BULLET_HEIGHT)

    def __init__(self, screen, ship):
        super().__init__()
        self.screen = screen

        self.rect = pygame.Rect((0, 0), self.DIMENSIONS)
        self.rect.centerx = ship.rect.centerx
        self.rect.bottom = ship.rect.top

        self.y = float(self.rect.y)

    def update(self):
        """Move bullet up"""
        self.y -= game_settings.SHIP_SPEED_FACTOR
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet on the screen"""
        pygame.draw.rect(self.screen, game_settings.BULLET_COLOR, self.rect)
