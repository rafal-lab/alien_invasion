import pygame.font

class Scoreboard:
    """Klasa przeznaczona do przedstawiania informacji o punktacji """

    def __init__(self, ai_game):
        """Initalization points atribut"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        #settings to punctation font
        self.text_color = (250,250,250)
        self.font = pygame.font.SysFont(None, 50)

        #prepering starting image witg points
        self.prep_score()

    def prep_score(self):
        """Przekształcenie punktacji na wygenerowany obraz"""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        #printing a score in top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.score_rect.right
        self.score_rect.top = 5

    def show_score(self):
        """wyswietlenie punktacji"""
        self.screen.blit(self.score_image, self.score_rect)