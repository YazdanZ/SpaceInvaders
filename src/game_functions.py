import sys
import pygame
from time import sleep

from bullet import Bullet
from alien import Alien
import settings as game_settings


def check_for_events(screen, ship, bullets):
    """Respond to keyboard and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        check_keydown_event(event, ship, screen, bullets)
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
        # TODO: add sound effect over here


def update_screen(screen, ship, bullets, aliens):
    """Redraw the screen and change to the new screen"""
    # redraw the screen
    screen.fill(game_settings.BG_COLOR)

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.draw()
    aliens.draw(screen)
    pygame.display.flip()


def update_bullets(bullets, aliens, screen, ship):
    """Update bullet positions"""
    # check for collisions
    if check_bullet_collision(bullets, aliens):
        create_alien_fleet(screen, ship, aliens)

    bullets.update()

    # delete bullets that go outside the screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def check_bullet_collision(bullets, aliens):
    pygame.sprite.groupcollide(bullets, aliens, True, True)

    if len(aliens) == 0:
        bullets.empty()
        return True


def create_alien_fleet(screen, ship, aliens):
    alien = Alien(screen)
    alien_width = alien.rect.width / 2
    number_of_rows = get_vertical_alien_number(ship.rect.height, alien.rect.height)

    for row_num in range(number_of_rows):
        for alien_num in range(get_horizontal_alien_number(alien_width)):
            create_alien(screen, aliens, alien_width, alien_num, row_num)


def get_horizontal_alien_number(alien_width):
    available_horizontal_space = game_settings.SCREEN_WIDTH - 2 * alien_width
    alien_number = int(available_horizontal_space / (2 * alien_width))
    return alien_number


def get_vertical_alien_number(ship_height, alien_height):
    """Determine the number of alien rows that fit on the screen"""
    available_vertical_space = (
        game_settings.SCREEN_HEIGHT - 3 * alien_height - ship_height
    )

    number_rows = int(available_vertical_space / (alien_height))
    return number_rows


def create_alien(screen, aliens, alien_width, alien_num, row_number):
    alien = Alien(screen)
    alien.x = alien_width + 2 * alien_width * alien_num
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height / 2 + 2 * alien.rect.height / 2 * row_number
    aliens.add(alien)


def update_aliens(aliens, ship, bullets, screen):
    """Update the alien fleet position"""
    check_fleet_edges(aliens)
    aliens.update()

    # alien ship collisions
    if pygame.sprite.spritecollideany(ship, aliens):
        hit_ship(aliens, bullets, screen, ship)


def hit_ship(aliens, bullets, screen, ship):
    """Respond to ship being hit by aliens"""
    create_alien_fleet(screen, ship, aliens)

    ship.center_ship()
    aliens.empty()
    bullets.empty()
    sleep(0.5)


def check_fleet_edges(aliens):
    for alien in aliens.sprites():
        if alien.check_edge_collision():
            change_fleet_direction(aliens)
            break


def change_fleet_direction(aliens):
    """Drop the fleet dows by a row and change directions"""
    for alien in aliens.sprites():
        alien.rect.y += game_settings.FLEET_SPEED
    game_settings.FLEET_DIRECTION *= -1
