# Arquivo principal do projeto

import pygame
import sys
from config import width, height, fps, black
import player
from menu import font, text_color, draw_text

# Iniciar Pygame
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Friends in the backrooms")
player.init_player()
clock = pygame.time.Clock()

# Variáveis do jogo
game_paused = False

# Loop principal
while True:
    dt = clock.tick(fps)
    # Checar se o jogo está pausado
    if game_paused == True:
        pass
        # Mostrar Menu
    else:
        draw_text("Pressione ESC para pausar", font, text_color, 360, 680)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_paused = True
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    # Atualizar e desenhar
    screen.fill(black)
    player.draw(screen, dt, keys)
    pygame.display.flip()