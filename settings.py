
#a class to store all settings for Alien Invasion

class Settings():

    def __init__(self):
        #Screen settings

        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)


        # Bullet settings
        self.bullet_speed_factor = 1 #pozicija keiciasi 1 pixeliu
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3 #3 bullet at the time

        #Alien settings

        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

        self.speedup_scale = 1.1 #tiek kartu padidina viskam greiti in increase_speed
        self.initialize_dynamic_settings()

        #Ship settings:

        self.ship_speed_factor = 1.5  # pozicija keiciasi 1.5 pixelio
        self.ship_limit = 3

        # How quickly the alien point values increase
        self.score_scale = 1.5

    def initialize_dynamic_settings(self): #siti values keisis kai level up
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.fleet_direction = 1
        self.alien_points = 50




    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        #kai call funkcija pakelti greiti, padideja gaunami taskai
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)