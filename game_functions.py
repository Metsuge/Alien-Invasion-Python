import sys      #import sys and pygame modules
from time import sleep
import pygame
from bullet import Bullet
from game_stats import GameStats
from alien import Alien

pygame.init()

def check_high_score(stats, sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()


def ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets):
    if stats.ships_left > 0: #jeigu yra daugiau nei 0, aliens atsiranda is naujo
        stats.ships_left -= 1
        sb.prep_ships()
        aliens.empty()
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        sleep(0.5)
    else: # jei 0 zaidimas baigiasi
        stats.game_active = False
        pygame.mouse.set_visible(True)

#tikrina ar aliens paliete screen bottom, jei taip - prasideda is naujo

def check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
            break #jei nors vienas pasieke - game over, nereikia loopint per visus aliens


def get_number_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height): #kiek eiliu aliens telpa ekrane
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):

    alien = Alien(ai_settings, screen) #padarom viena alien kad zinot ilgi auksti
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width) #pagal ta viena alien skaiciuojam
    #kiek aliens tilps i viena eile
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    for row_number in range(number_rows):#outer loop couts how many rows of alines
        #inner loop creates aliens for each row
        for alien_number in range(number_aliens_x): # for very alien in hoewerver much there are in number_alien_x do this:
            create_alien(ai_settings, screen, aliens, alien_number, row_number) # create that many an aliens


def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:  # jei ekrane esanciu kulku maziau nei 3 tada varom toliau
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)  # Create a new bullet and add it to the bullets group.




# ~~~~~~~~~~~~~~MOVING UP and DOWN~~~~~~~~~~~~~~~~
    #if event.key == pygame.K_UP: #jei nebespaudi i virsu tada judejimas False
        #ship.moving_up = False

    #if event.key == pygame.K_DOWN: #jei nebespaudi zemyn tada judejimas False
       # ship.moving_down = False
# ~~~~~~~~~~~~~~MOVING UP and DOWN~~~~~~~~~~~~~~~~


def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):

    for event in pygame.event.get(): #method event.get() registruoja visus paspaudimus
        if event.type == pygame.QUIT: #jei paspaus x ekrano kampe uzdaryti
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:#siaip reaguoja paspaudus belekur, bet galima sukonkretint
            mouse_x, mouse_y = pygame.mouse.get_pos() #surandam, kur pele kai ja paspaudi
            check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)
            #patiktina, ar paspaude ten kur reikia, siuncia i funkcija

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets) #referuoja i keydown funkcija 8 eilute

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship) #referuoja i keyup funkcija 14 eilute


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
         ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True  # True kol laikomas nuspaustas mygtukas
    elif event.key == pygame.K_LEFT:
            ship.moving_left = True

    elif event.key == pygame.K_SPACE: #kai spaudi space, tikrina, kiek jau yra bullets:
        fire_bullet(ai_settings, screen, ship, bullets)

    elif event.key == pygame.K_q:
        sys.exit()


def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        ai_settings.initialize_dynamic_settings()
        pygame.mouse.set_visible(False)#invisible cursor
        stats.reset_stats() #3 nauji ships again
        stats.game_active = True #game starts as soon as this function ends

        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        aliens.empty()
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()


def check_fleet_edges(ai_settings, aliens):
    for alien in aliens.sprites(): #kiekviena alien tikrina pagal check edges, ar jis islipes uz ribu
        if alien.check_edges():#if True, call change fleet directions
            change_fleet_direction(ai_settings, aliens)
            break #break out of loop
def change_fleet_direction(ai_settings, aliens):
    for alien in aliens.sprites(): #loop through all aliens and drop them
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1 #jei buvo 1*-1 = -1 / -1 * - 1 = 1, pasikeis kryptis bet kokiu atveju


def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        stats.score += ai_settings.alien_points
        sb.prep_score() #update score

    check_high_score(stats, sb)

    if len(aliens) == 0:

        bullets.empty()
        ai_settings.increase_speed()

        stats.level += 1
        sb.prep_level()

        create_fleet(ai_settings, screen, ship, aliens)


def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0: #jei pasiekia y asi pradingsta
            bullets.remove(bullet)

    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)


def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button): #pridedam papildomi parameter kad nupiestu dalykus ant ekrano

    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():  #ekrane piesia ne tik ta kuria katik paleido bet visas paleistas bullets
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    sb.show_score() #call to function in scoreboard to show score
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()


def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets): # kam tas update?
    check_fleet_edges(ai_settings, aliens)
    aliens.update()


    if pygame.sprite.spritecollideany(ship, aliens): #sitas metodas tikrina ar yra any collisions
        ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)

    check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets) #ar aliens pasieka screen bottom