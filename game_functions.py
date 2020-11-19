import sys
import pygame


def check_for_events():
    """Respond to keyboard and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(game_settings, screen, ship):
    """Redraw the screen and change to the new screen"""
    # redraw the screen
    screen.fill(game_settings.bg_color)
    ship.blit()
    pygame.display.flip()
