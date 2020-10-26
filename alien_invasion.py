import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #创建Play按钮
    play_button = Button(ai_settings, screen, "Play")

    #创建一艘飞船
    ship = Ship(ai_settings, screen)

    #创建一个用于存储子弹的编组
    bullets = Group()

    aliens = Group()

    #创建外星人
    gf.create_fleet(ai_settings, screen, ship, aliens)

    #创建一个用于存储游戏统计信息的实例并创建计分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            #隐藏光标
            pygame.mouse.set_visible(False)

            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
run_game()