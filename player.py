# Arquivo: player.py
import pygame
from config import width, height

# Variáveis globais do player
player_x = 100
player_y = 100
player_speed = 3

# Controle de animação
current_frame = 0
frame_timer = 0
frame_duration = 200

# Sprites
idle_image = None
walk_images = []

# Inicialização dos sprites (chamar após criar a tela no main)
def init_player():
    global idle_image, walk_images
    idle_image = pygame.image.load("assets/img/player_idle.png").convert_alpha()
    walk1 = pygame.image.load("assets/img/player_walk1.png").convert_alpha()
    walk2 = pygame.image.load("assets/img/player_walk2.png").convert_alpha()
    walk_images = [walk1, walk2]

# Movimentação do jogador
def handle_movement(keys):
    global player_x, player_y
    moving = False

    if keys[pygame.K_w] and player_y > 0:
        player_y -= player_speed
        moving = True
    if keys[pygame.K_a] and player_x > 0:
        player_x -= player_speed
        moving = True
    if keys[pygame.K_s] and player_y < height - idle_image.get_height():
        player_y += player_speed
        moving = True
    if keys[pygame.K_d] and player_x < width - idle_image.get_width():
        player_x += player_speed
        moving = True

    return moving

# Atualiza animação e retorna a imagem correta
def update_animation(dt, moving):
    global current_frame, frame_timer

    if moving:
        frame_timer += dt
        if frame_timer >= frame_duration:
            frame_timer = 0
            current_frame = (current_frame + 1) % len(walk_images)
        return walk_images[current_frame]
    else:
        current_frame = 0
        frame_timer = 0
        return idle_image

# Função principal para desenhar o player
def draw(screen, dt, keys):
    moving = handle_movement(keys)
    current_img = update_animation(dt, moving)
    screen.blit(current_img, (player_x, player_y))

# Função para obter posição atual (opcional)
def get_position():
    return player_x, player_y