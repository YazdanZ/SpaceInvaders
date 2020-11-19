import sys
import pygame


def check_for_events(ship):
    """Respond to keyboard and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            if event.key == pygame.K_LEFT:
                ship.moving_left = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            if event.key == pygame.K_LEFT:
                ship.moving_left = False


def update_screen(game_settings, screen, ship):
    """Redraw the screen and change to the new screen"""
    # redraw the screen
    screen.fill(game_settings.BG_COLOR)
    ship.blit()
    pygame.display.flip()
