import sys
import pygame
from settings import Settings


def run_game():
    game_settings = Settings()

    # initialize game and create s screen
    pygame.init()
    screen = pygame.display.set_mode(
            (game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Space Invaders")

    # main loop of the game
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(game_settings.bg_color)
        pygame.display.flip()


run_game()
