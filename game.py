import pygame
from pygame.sprite import Group

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

    # group of bullets
    bullets = Group()

    # main loop of the game
    while True:
        game_functions.check_for_events(screen, ship, bullets)
        ship.update()
        game_functions.update_bullets(bullets)
        game_functions.update_screen(screen, ship, bullets)


run_game()
