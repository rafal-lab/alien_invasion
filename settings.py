class Settings:
    '''Klasa przeznaczona do przechowywania ustawien gry'''

    def __init__(self):
        '''Inicjalizacja ustawien gry'''
        # ustawienia ekranu
        self.screen_width = 1350
        self.screen_height = 700
        self.bg_color = (160, 200, 255)

        # ustawienia statku
        self.ship_limit = 2

        # usawienia pocisku

        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_alowed = 3

        # ustawienai obcych
        self.fleet_drop_speed = 10

        self.initialize_dynamic_settings()
        #change game speed
        self.speedup_scale = 1.1
        #change point for killing
        self.score_scale = 1.5



    def initialize_dynamic_settings(self):
        """Ustawienie ulegajace zmianie w czasie gry"""
        self.ship_speed = 1.5
        self.alien_speed = 0.3
        self.bullet_speed = 1.0

        # 1 oznacza prawo , -1 lewo
        self.fleet_direction = 1
        #punktacja
        self.alien_points = 50

    def increase_speed(self):
        """zmiana ustawien dotyczacych szybkosci"""
        self.ship_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
