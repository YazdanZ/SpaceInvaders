import pygame

from ship import Ship
import game_functions
import settings as game_settings


def run_game():

    # initialize game and create s screen
    pygame.init()
    screen = pygame.display.set_mode(
            (game_settings.SCREEN_WIDTH, game_settings.SCREEN_HEIGHT))
    pygame.display.set_caption("Space Invaders")

    ship = Ship(screen)

    # main loop of the game
    while True:
        game_functions.check_for_events(ship)
        ship.update()
        game_functions.update_screen(game_settings, screen, ship)


run_game()
