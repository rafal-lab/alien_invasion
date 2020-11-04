class GameStats():
    """Monitotorowanie danych statystycznych w grze inwazja obcych"""

    def __init__(self, ai_game):
        """Inicjalizacja danych statystycznych"""
        self.settings = ai_game.settings
        self.reset_stats()
        #uruchomienie gry w stanie aktywnym
        self.game_active = False
        with open('highest_score', "r") as f:
            high_score = f.read()
            print(high_score)
        self.high_score = int(high_score)
    def reset_stats(self):
        """Inicjalizacja danych ktore moga zmieniac sie w trakcie gry"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
