import pygame
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from button import Button

def run_game():
    #inicia o pygame, as configurações, a tela e demais superfícies
    pygame.init()
    settings = Settings()

    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Cria o botão Play
    play_button = Button(settings, screen, "Jogar")

    # Cria uma instância para armazenar dados estatísticos do jogo e cria painel de pontuação
    stats = GameStats(settings)
    sb = Scoreboard(settings, screen, stats)

    # Cria uma espaçonave
    ship = Ship(settings, screen)
    # Cria um grupo no qual serão armazenados os projéteis

    bullets = Group()
    # Cria um alienígena
    aliens = Group()

    # Cria uma frota de alienígenas
    gf.create_fleet(settings, screen, ship, aliens)

    #inicia o laço principal do jogo
    while True:
        gf.check_events(settings, screen, stats, sb, play_button, ship, aliens, bullets)
        gf.update_screen(settings, screen, sb, ship, stats, aliens, bullets, play_button)

        if stats.game_active:
            ship.update()
            gf.update_bullets(settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(settings, stats, screen, sb, ship, aliens, bullets)
            
run_game()