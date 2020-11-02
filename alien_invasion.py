import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from time import sleep
from game_stats import GameStats
from button import Button

class AlienInvasion:
    """Klasa służaca do zarzadzania zasobami i sposobem działania gry  """

    def __init__(self):
        """Inicjalizacja gry i utworzenie jej zasoboów"""
        pygame.init()  # wyswietlanie tła
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)# krotka definiujaca fullscrena
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Inwazja obcych")

        #dane statystyczne w grze
        self.stats = GameStats(self)

        self.ship = Ship(self)  # utworzenie egemplrza klasy SHIP, wymaga przekazania obiektu klasy alieninvasion
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        #utworzenie przycisku
        self.play_button = Button(self, msg="Graj")

    def run_game(self):
        """Rozpoczecie petli głownej gry."""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._bullet_update()
                self._update_aliens()

            self._update_screen()


    def _ship_hit(self):
        """reakcaj na uderzenie obcego w statek"""
        if self.stats.ships_left > 0:
            #zmniejszenie wartosci ships_left
            self.stats.ships_left -=1

            #usuniecie obcych i pociskow
            self.aliens.empty()
            self.bullets.empty()

            #utworzenie zawartosci listy aliens i bullets
            self._create_fleet()
            self.ship.center_ship()

            sleep(0.5)

        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _create_fleet(self):
        """Utworzenie pelnej floty obcych"""
        #utworzenie obcego, i okreslenei ile obcych miesci sie w rzedzie
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (4 * alien_width)
        number_aliens_x = available_space_x // (2*alien_width)

        #usalenie ile rzedow obcych zmiesci sie na ekranie
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height-(5*alien_height) - ship_height)
        number_rows = available_space_y //(2 * alien_height)

        #pierwszy rzad obcych
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                #tworzymy obecego i umieszczamy w rzedzie
                self._create_alien(alien_number, row_number)


    def _create_alien(self,alien_number, row_number):
        """Utworzenie obcego i umieszczenie go w rzedzie"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2*alien.rect.height * row_number
        self.aliens.add(alien)

    def _bullet_update(self):
        """Uaktualnienie polozenia pociskow i usniecie tych nie widocznych"""
        # uaktualnia polozenie
        self.bullets.update()

        # usuniecie pociskow poza ekranem
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisins()

    def _check_aliens_bottom(self):
        """sprawdzenie czy ktory kolwiek obcy dotarl do dolnej krawedzi ekranu"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

    def _check_bullet_alien_collisins(self):
        # sprawdzanie czy pocisk trafil obcego, jesli tak osuwamy i pocisk i obcego
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if not self.aliens:
            # pozbycie sie pociskow i utworzenie nowej floty
            self.bullets.empty()
            self._create_fleet()

    def _check_events(self):
        """_metoda pomocnicza nie do wywołania dla egemplarza klasy"""
        """Reakcja na zdarzenie klawiatury i myszy"""

        for event in pygame.event.get():  # petla zdarzen
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:  # sprawdzamy nacisniecie klawisz
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:  # jesli klawisz podniesiony t
                # o nie przesuwamy
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_keydown_events(self, event):
        """Reakacja na nacisniecie klawisza"""
        if event.key == pygame.K_RIGHT:  # czy nacisniety klawisz to prawy kursor
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

        elif event.key == pygame.K_q:  # zamkniecie w przypadku wcisniecia q
            sys.exit()

    def _check_keyup_events(self, event):
        """Reakcja na zwolnienie klawisz"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _check_play_button(self, mouse_pos):
        """rozpoczecie nowej gry po wcisnieciu przycisku"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.stats.reset_stats()
            self.stats.game_active = True

            #usuniecie listy aliens i bullets
            self.aliens.empty()
            self.bullets.empty()

            #utworzenie nowej floty i wysrodkowanie statku
            self._create_fleet()
            self.ship.center_ship()

            #ukrycie kursora myszy
            pygame.mouse.set_visible(False)



    def _fire_bullet(self):
        """Utworzenie nowego pocisku i dodanie go do grupy pociskow"""
        if len(self.bullets) < self.settings.bullet_alowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_screen(self):
        """Uaktualnianie obrazu na ekranie"""
        # odswiezanie ekranu
        self.screen.fill(self.settings.bg_color)  # definicja tła
        self.ship.blitme()  # wyswietlenie statkum nad tłem
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)

        #wyswietlenie przycisku tylko gdy gra nie aktywna
        if not  self.stats.game_active:
            self.play_button.draw_button()
        # wyswietlenie ostatnio zmodyfikowanego ekranu, odswiezanie ekranu
        pygame.display.flip()



    def _update_aliens(self):
        """Uaktualnienie polozenie wszystkich obcych we flocie"""
        self._check_fleet_edges()
        self.aliens.update()

        #wykrywanie kolizji miedzy obcym i statkiem
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        #wyszukanie obcych uderzajcych w dolna krawedz
        self._check_aliens_bottom()




    def _check_fleet_edges(self):
        """Odpowiednia reakcja gdy opcy dotrze do krawedzi ekranu"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """przesuniecie floty w dol i zmiana kierunku"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

if __name__ == '__main__':
    # utworzenie egzemplarza gry i jej uruchomiemie
    ai = AlienInvasion()
    ai.run_game()
