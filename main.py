import pygame
import sys
from config import width, height, fps, black
from config import width, height
import map
import player
from menu import font, text_color, draw_text

# Inicialização
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("liminal_1987-12-03")
clock = pygame.time.Clock()

# Imagens
floor_img = pygame.image.load("assets/img/floor.png").convert()
wall_img = pygame.image.load("assets/img/wall.png").convert()

# Carregar sprites do jogador
idle_img, walk_imgs = player.load_images()

# Carregar mapa (com chão + paredes)
wall_rects, tiles_to_draw = map.load_map(floor_img, wall_img)

# Loop do jogo
while True:
    dt = clock.tick(fps)
    # Checar se o jogo está pausado
    if game_paused == True:
        pass
        # Mostrar Menu
    else:
        draw_text("Pressione ESC para pausar", font, text_color, 360, 680)
    dt = clock.tick(165)
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
    # Desenhar fundo do mapa
    for img, pos in tiles_to_draw:
        screen.blit(img, pos)

    # Atualizar e desenhar player
    player.draw(screen, dt, keys, wall_rects, idle_img, walk_imgs)  # Passando as imagens carregadas

    pygame.display.flip()
