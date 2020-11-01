
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Klasa przedsawia pojedynczego obcego we flocie"""

    def __init__(self, ai_game):
        """Inicjalizacja obcego i zdefinioweanie jego polozenia poczatkowego """
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #wczytanie obrazu obcego i okreslenie jego atrybutow rect
        self.image = pygame.image.load('images/alien.bmp')
        self.image = pygame.transform.scale(self.image, (45,45))
        self.rect = self.image.get_rect()

        #umieszczeeni obcego wl ewym rogu
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #przechowywanie dokladnego polozenia obcego
        self.x = float(self.rect.x)

    def update(self):
        """przesuniecie obcego w prawo"""
        self.x += (self.settings.alien_speed *self.settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """Zwraca tru jesli obcy jest przy krawedzi ekranu"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <=0:
            return True