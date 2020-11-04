import pygame.font
from pygame.sprite import Group
from ship import Ship
from settings import Settings

class Scoreboard:
    """Klasa przeznaczona do przedstawiania informacji o punktacji """

    def __init__(self, ai_game):
        """Initalization points atribut"""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        #settings to punctation font
        self.text_color = (250,250,250)
        self.font = pygame.font.SysFont(None, 50)

        #prepering starting image witg points
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_ships(self):
        """wyswietla liczbe statkow pozostała graczowi"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left+1):
            ship = Ship(self.ai_game)
            settings = Settings()
            ship.rect.x = settings.screen_width - (ship_number+1) * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)


    def prep_level(self):
        """Konwersja numeru poziomu na obraz"""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)

        #numer poziomu jest wyswietlany pod akutalna punktacja
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_score(self):
        """Przekształcenie punktacji na wygenerowany obraz"""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        #printing a score in top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.score_rect.right
        self.score_rect.top = 5

    def prep_high_score(self):
        """printing the highest score in the game"""
        #high_score = round(self.stats.high_score, -1)

        high_score_str = "{:,}".format(self.stats.high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)

        #wyswietlanie najlepszego wyniku
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.score_rect.top+ 750
        self.high_score_rect.top = self.score_rect.top

    def show_score(self):
        """wyswietlenie punktacji"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

    def check_high_score(self):
        """checking if actual score is the best"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
            with open('highest_score', 'w') as f:
                f.write(str(self.stats.high_score))
