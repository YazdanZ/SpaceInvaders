import pygame
from pygame.sprite import Group

from ship import Ship
import game_functions
import settings as game_settings


def run_game():

    # initialize game and create s screen
    pygame.init()
    screen = pygame.display.set_mode(
        (game_settings.SCREEN_WIDTH, game_settings.SCREEN_HEIGHT)
    )
    pygame.display.set_caption("Space Invaders")

    ship = Ship(screen)

    # group of bullets and aliens
    bullets = Group()
    aliens = Group()

    game_functions.create_alien_fleet(screen, ship, aliens)

    # main loop of the game
    while True:
        game_functions.check_for_events(screen, ship, bullets)
        ship.update()
        game_functions.update_bullets(bullets, aliens, screen, ship)
        game_functions.update_aliens(aliens)
        game_functions.update_screen(screen, ship, bullets, aliens)


run_game()
