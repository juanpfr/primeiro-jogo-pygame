# Arquivo principal do projeto

import pygame
import sys
from config import width, height, fps, white
import player

# Iniciar Pygame
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Friends in the backrooms")
player.init_player()
clock = pygame.time.Clock()

# Loop principal
while True:
    dt = clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    # Atualizar e desenhar
    screen.fill(white)
    player.draw(screen, dt, keys)
    pygame.display.flip()