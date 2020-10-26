class Settings():

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        #子弹设置
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        #外星人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 3
        self.fleet_direction = 1 #fleet_direction为1表示右移，为-1表示左移

        #以什么样子的速度加快游戏节奏
        self.speedup_scale = 1.1

        #外星人点数的提高速度
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

        #计分
        self.alien_points = 50

    def initialize_dynamic_settings(self):
        #初始化随着游戏进行而变化的设置
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        self.fleet_direction = 1

    def increase_speed(self):
        #提高速度设置和外星人点数
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)