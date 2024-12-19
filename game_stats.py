class GameStats():
    """Armazena dados estatísticos da Invasão Alienígena."""
    def __init__(self, settings):
        """Inicializa os dados estatísticos."""
        self.settings = settings
        self.reset_stats()

        # Inicia a Invasão Alienígena em um estado inativo
        self.game_active = False

    def reset_stats(self):
        """Inicializa os dados estatísticos que podem mudar durante o jogo."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1