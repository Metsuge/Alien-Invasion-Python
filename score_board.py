import pygame.font #writes text to screen

from pygame.sprite import Group
from ship import Ship

class Scoreboard():
    def __init__(self, ai_settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        self.prep_score() #text to be displayed into image, funkcija the following:
        self.prep_high_score() #atskirai rodys highscore
        self.prep_level()
        self.prep_ships()

    def prep_ships(self): #padaro grupe kuri laikys laivu instanses
        self.ships = Group()
        for ship_number in range(self.stats.ships_left): #grupeje bus kiekvienas ship, kurio dar nepanaudojo
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)



    def prep_level(self):
        #padaro imga is surinto score kuris yra saugomas stats.level
        self.level_image = self.font.render(str(self.stats.level), True, self.text_color, self.ai_settings.bg_color)

        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right #kad butu on the right kaip ir score rodomas
        self.level_rect.top = self.score_rect.bottom + 10 #10 px po apacia nuo score


    def prep_high_score(self):
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True,self.text_color, self.ai_settings.bg_color)

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top


    def prep_score(self):
        score_str = str(self.stats.score) #skaicius padarom string ir perduodam render kad is to padarytu image
        #suapvalinti skaicius ir idet taskus kai didelis sk.
        rounded_score = round(self.stats.score, -1) #round nr to nearest 10
        score_str = "{:,}".format(rounded_score)

        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

        #kad reguliuoti, kur tas image buna, pasidarom image rect
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20 #image is 20px from screens right edge
        self.score_rect.top = 20 # ant 20pc from screens top


    def show_score(self): #display image on screen
        self.screen.blit(self.score_image, self.score_rect) #draws score
        self.screen.blit(self.high_score_image, self.high_score_rect) #draws high score
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)