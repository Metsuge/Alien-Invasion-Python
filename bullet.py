import pygame

from pygame.sprite import Sprite
#Sprite class yra pygame dalis, sprite gali importuoti


class Bullet(Sprite):

    def __init__(self, ai_settings, screen, ship):

        super(Bullet, self).__init__()
        self.screen = screen

        #sukuria bullet rect, darom rect from scratch su pygame.Rect
        #Rect() klasei reikia x ir y koords top left korner (nes nuo top left pradeda skaiciuoti viska)
        #ir  plocio su aukscio
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)

        #bullets x asies vidurys lygis ships x asies vidurui, kad ne is kampo eitu kulka o per vidury
        self.rect.centerx = ship.rect.centerx
        #kulkos judejimas pasideda nuo ships top, islenda is virsaus laivo
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y) # kad zinot kur kulka yra y asyje (aukstyn-zemyn) kad reguliuoti greiti
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        self.y -= self.speed_factor #kad kulka judetu aukstyn-zemyn
        self.rect.y = self.y #update kulkos koords

#piesiam bullet. sitas metodas uzpildo ta nurodyta kvardraciuka pasirinkta spalva
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)