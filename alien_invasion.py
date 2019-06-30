import pygame #pygame turi functionality needed to make a game

from pygame.sprite import Group

from settings import Settings

from ship import Ship

from game_stats import GameStats

from button import Button

from score_board import Scoreboard

import game_functions as gf

def run_game():

    pygame.init() # Initializes background settings for Pygame to work
    ai_settings = Settings()
    # we call pygame.display.set_mode to create a display window(screen), arguments are access  to file Settings
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    play_button = Button(ai_settings, screen, "Play")

    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    #make a shipSC

    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    while True:  #the game is controlled by a this loop. It contains event loop and code that manages screen updates
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets) #everything is in game_functions kur yra event loop called check_events
        #tikrinam paspaudimus nors zaidimas neveikia, gali paspausti quit pvz


        if stats.game_active: #ijungti tik kai True
            ship.update()
        #pirma tikrina kulkas, tada ateivius
        #nes tikrinsim ar kulkos paliete ateivius
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)

     #referuoja i skilti apie bullets in game_functions imported as gf
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
        ship.blitme()

        pygame.display.flip() # Make the most recently drawn screen visible

run_game()