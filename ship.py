import pygame

from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self, ai_settings, screen):  #ship and set its starting position ai_settings is the file Settings

        super(Ship, self).__init__() #to make Ship inherit from Sprite

        # variable
        self.screen = screen #value

        self.ai_settings = ai_settings

        # returns a surface representing the ship which is stored in self.image
        self.image = pygame.image.load('images/ufo.bmp') #image loaded with pygame.image.load and stored in self.image



        self.rect = self.image.get_rect()  #rect image per savybe rect padaryta i rectangular thing that is the image
        #self.rect dabar ir yra tas image
        self.screen_rect = screen.get_rect() #the same. self.scree_rect yra monitorius su rect savybe

    #padaro, kad originally image is on the bottom in the middle of the screen
        self.rect.centerx = self.screen_rect.centerx  #centerx yra, reikia dar centery atsirandta apacioj vidury
        #centery yra bottom
        self.rect.bottom = self.screen_rect.bottom #image apacia lygi su screen apacia


        self.center = float(self.rect.centerx) #laivo centro padetis x asyje kad zinot kur jis ir kad neislektu is ribu


# ~~~~~~~~~~~~~~MOVING UP and DOWN v v v v~~~~~~~~~~~~~~~~
        self.y = float(self.rect.centery)



        self.screen_top = self.screen_rect.top


        #default kad niekad nejuda kol nieko nedarai

        self.moving_right = False
        self.moving_left = False

       # self.moving_up = False
        #self.moving_down = False

# ~~~~~~~~~~~~~~MOVING UP and DOWN ^ ^  ^^ ^^^ ~~~~~~~~~~~~~~~~

    def update(self):

        #if right keydown and ships right krastines koordinates mazesnes nei ekrano right krastines koord:
        #ship centro judejimas yra True ir jis juda greiciu ==  self.ai_settings.ship_speed_factor

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        #jeigu left ketdoen ir kaires krastines koordinates daugiau nei 0:
        #judam kairen

        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center



#~~~~~~~~~~~~~~MOVING UP and DOWN~~~~~~~~~~~~~~~~
        #self.rect.centery = self.y   #pajamam y koordinate kuri yra aukstyn-zemyn
        # jei judant virsus dar nepasieke sceen virsaus judam toliau
        #if self.moving_up and self.rect.top != self.screen_rect.top:
            #self.y -= self.ai_settings.ship_speed_factor #image centriukas juda 1.5 px greiciu y koordinate

        # jei image apacia dar nepasieke screen apacios, juda toliau
        #if self.moving_down and self.rect.bottom != self.screen_rect.bottom:
            #self.y += self.ai_settings.ship_speed_factor

# ~~~~~~~~~~~~~~MOVING UP and DOWN~~~~~~~~~~~~~~~~
    def blitme(self): #nupies image on the screen
        self.screen.blit(self.image, self.rect)

    def center_ship(self):#center the ship when aliens touch ship and disapear
        self.center = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
