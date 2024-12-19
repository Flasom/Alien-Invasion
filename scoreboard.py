import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard():
    """Uma classe para mostrar informações sobre pontuação"""

    def __init__(self, settings, screen, stats):
        """Inicializa os atributos da pontuação"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings
        self.stats = stats

        # Configurações de fonte para as informações de pontuação
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepara a imagem da pontuação inicial
        self.prep_score()
        self.prep_level()
        self.prep_ships()

    def prep_ships(self):
        """Mostra quantas espaçonaves restam"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def prep_score(self):
        """Transforma a pontuação em uma imagem renderizada"""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(
            score_str, True, self.text_color, self.settings.bg_color)

        # Exibe a pontuação na parte superior direita da tela
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_level(self):
        """Transforma o nível em uma imagem renderizada"""
        self.level_image = self.font.render(
            str(self.stats.level), True, self.text_color, self.settings.bg_color)

        # Posiciona o nível abaixo da pontuação
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def show_score(self):
        """Desenha a pontuação na tela."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        # Desenha as espaçonaves
        self.ships.draw(self.screen)
