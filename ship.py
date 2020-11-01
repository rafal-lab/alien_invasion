import pygame

class Ship:
    '''Klasa przeznaczona do zarzadzania statkiem kosmicznym'''

    def __init__(self, ai_game): #ai_game odwolanie do elementu klasy alien_inaasion
        '''Inicjalizacja statku kosmicznego i jego polozenia poczatkowego'''

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect() #rect pozwala traktowac element jako prostokat


        #wczytywanie obrazu statku kosmicznego i pobrannie jego prostokata
        self.image = pygame.image.load('images/ship.bmp')
        self.image= pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect() #pobiera polozenie statku

        #kazdy nowy statek kosmiczny pojawia sie na srodkowymdole ekranu
        self.rect.midbottom = self.screen_rect.midbottom

        #polozenie poziome statku jest przechowywane w floacie
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        #opcja wskazujaca na poruszanie statku
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        '''Uaktaulnienie polozenie satku na podstawie opcji wskazujacej jego ruch'''
        #poczatek lewy rog ekranu (0,0)
        # sprawdzamy czy statek dotarł do krawedzi. selfr.rect.right - prawa wspolrzedna prostkata
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        elif self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        elif self.moving_up and self.rect.top > 0: #ruch w gore
            self.y -= self.settings.ship_speed
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom: #ruch w dol
            self.y += self.settings.ship_speed

        #uaktualnianie obiektu na podstawie wartosci self.x
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        '''Wyswietlenie statku kosmicznego w jego aktualnym polozeniu'''
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Umieszczeenie statku na srodku """
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)