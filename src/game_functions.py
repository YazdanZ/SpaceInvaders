import sys
import pygame

from bullet import Bullet
import settings as game_settings


def check_for_events(screen, ship, bullets):
    """Respond to keyboard and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        check_keydown_event(event, ship, screen,  bullets)
        check_keyup_event(event, ship)


def check_keyup_event(event, ship):
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            ship.moving_left = False


def check_keydown_event(event, ship, screen, bullets):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            ship.moving_right = True
        if event.key == pygame.K_LEFT:
            ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            fire_bullet(screen, ship, bullets)


def fire_bullet(screen, ship, bullets):
    if len(bullets) < game_settings.BULLETS_ALLOWED_ON_SCREEN:
        bullet = Bullet(screen, ship)
        bullets.add(bullet)


def update_screen(screen, ship, bullets, alien):
    """Redraw the screen and change to the new screen"""
    # redraw the screen
    screen.fill(game_settings.BG_COLOR)

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.draw()
    alien.draw()
    pygame.display.flip()


def update_bullets(bullets):
    """Update bullet positions"""
    bullets.update()

    # delete bullets that go outside the screen
    for bullet in bullets.copy():
        if(bullet.rect.bottom <= 0):
            bullets.remove(bullet)
