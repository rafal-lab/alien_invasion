class Settings:
    '''Klasa przeznaczona do przechowywania ustawien gry'''

    def __init__(self):
        '''Inicjalizacja ustawien gry'''
        #ustawienia ekranu
        self.screen_width = 1350
        self.screen_height = 700
        self.bg_color = (160,200,255)

        #ustawienia statku
        self.ship_speed = 1.5
        self.ship_limit = 3

        #usawienia pocisku
        self.bullet_speed = 2.0
        self.bullet_width = 150
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_alowed = 3

        #ustawienai obcych
        self.alien_speed = 0.6
        self.fleet_drop_speed = 50
        # 1 oznacza prawo , -1 lewo
        self.fleet_direction = 1
