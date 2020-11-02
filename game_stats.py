class GameStats():
    """Monitotorowanie danych statystycznych w grze inwazja obcych"""

    def __init__(self, ai_game):
        """Inicjalizacja danych statystycznych"""
        self.settings = ai_game.settings
        self.reset_stats()
        #uruchomienie gry w stanie aktywnym
        self.game_active = False

    def reset_stats(self):
        """Inicjalizacja danych ktore moga zmieniac sie w trakcie gry"""
        self.ships_left = self.settings.ship_limit
        self.score = 0