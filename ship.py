import pygame


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

        # movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the position based on movement flags"""
        if self.moving_right:
            self.rect.centerx += 1

        if self.moving_left:
            self.rect.centerx -= 1

    def blit(self):
        """Draw the ship on its current location"""
        self.screen.blit(self.image, self.rect)
