import pygame
import settings as game_settings


class Ship:

    DIMENSIONS = (60, 60)

    def __init__(self, screen):
        """Initialize the ship and set it to its starting position"""
        self.screen = screen

        # load the ship image
        self.image = pygame.image.load('images/ship.bmp')
        self.image = pygame.transform.scale(self.image, Ship.DIMENSIONS)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # start the ship in the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.centerx = float(self.rect.centerx)

        # movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the position based on movement flags"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += game_settings.SHIP_SPEED_FACTOR

        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.centerx -= game_settings.SHIP_SPEED_FACTOR

        self.rect.centerx = self.centerx

    def blit(self):
        """Draw the ship on its current location"""
        self.screen.blit(self.image, self.rect)
