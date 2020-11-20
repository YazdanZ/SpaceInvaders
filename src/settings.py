import settings as game_settings


# display settings
SCREEN_WIDTH = 650
SCREEN_HEIGHT = 650
BG_COLOR = (52, 65, 87)

# ship settings
SHIP_SPEED_FACTOR = 0.4

# bullet settings
BULLETS_ALLOWED_ON_SCREEN = 4
BULLET_SPEED_FACTOR = 2
BULLET_WIDTH = 2
BULLET_HEIGHT = 12
BULLET_COLOR = (40, 140, 0)

# alien settings
ALIEN_SPEED_FACTOR = 0.175
FLEET_DIRECTION = 1
FLEET_SPEED = 10

# game speed
GAME_SPEEDUP = 1.05


class DynamicSettings:
    def __init__(self):
        self.game_speedup = game_settings.GAME_SPEEDUP
        self.alien_speed_factor = game_settings.ALIEN_SPEED_FACTOR

    def speedup_game(self):
        self.alien_speed_factor *= self.GAME_SPEEDUP
