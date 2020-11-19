import pygame

from settings import Settings
from ship import Ship
import game_functions


def run_game():
    game_settings = Settings()

    # initialize game and create s screen
    pygame.init()
    screen = pygame.display.set_mode(
            (game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Space Invaders")

    ship = Ship(screen)

    # main loop of the game
    while True:
        game_functions.check_for_events()
        game_functions.update_screen(game_settings, screen, ship)


run_game()
