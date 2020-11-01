import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''Klasa do zarzadzania posciskami wystrzelonymi przez statek'''

    def __init__(self, ai_game):
        """Utworzenie obiektu pocisku w aktualnym polozeniu statku"""
        super().__init__() #dziedziczy z SPrite
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #utworzenie prostokata pocisku w punkcie (0,0) a nastepnie zdefiniowanie dla niego odpowiedniego polozenia
        self.rect = pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        #polozenie pocisku jest zdefiniowane za pomoca wartosci zmiennoprzecinkowej
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def update(self):
        """Porszuanie pocisku po ekranie"""
        #uaktualnianie połozenia pocisku
        self.y -= self.settings.bullet_speed
        #uaktualnianie połozenia prostokąta pocisku
        self.rect.y = self.y

    def draw_bullet(self):
        """Wyswietlanie pocisku na ekranie"""
        pygame.draw.rect(self.screen, self.color, self.rect)

