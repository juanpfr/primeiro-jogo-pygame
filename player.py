# player.py

import pygame
from config import width, height

# Carregar sprites
def load_images():
    idle = pygame.image.load("assets/img/player_idle.png").convert_alpha()
    walk1 = pygame.image.load("assets/img/player_walk1.png").convert_alpha()
    walk2 = pygame.image.load("assets/img/player_walk2.png").convert_alpha()
    return idle, [walk1, walk2]

# Variáveis globais de posição e animação
player_x = 100
player_y = 100
player_speed = 3

# Controle de animação
current_frame = 0
frame_timer = 0
frame_duration = 200

# Função para movimentar o player
def handle_movement(keys, idle_img):
    global player_x, player_y
    moving = False

    if keys[pygame.K_w] and player_y > 0:
        player_y -= player_speed
        moving = True
    if keys[pygame.K_a] and player_x > 0:
        player_x -= player_speed
        moving = True
    if keys[pygame.K_s] and player_y < height - idle_img.get_height():
        player_y += player_speed
        moving = True
    if keys[pygame.K_d] and player_x < width - idle_img.get_width():
        player_x += player_speed
        moving = True

    return moving

# Função para atualizar a animação do player
def update_animation(dt, moving, walk_imgs, idle_img):
    global current_frame, frame_timer
    if moving:
        frame_timer += dt
        if frame_timer >= frame_duration:
            frame_timer = 0
            current_frame = (current_frame + 1) % len(walk_imgs)
        return walk_imgs[current_frame]
    else:
        current_frame = 0
        frame_timer = 0
        return idle_img

# Função para desenhar o player na tela
def draw(screen, dt, keys, wall_rects, idle_img, walk_imgs):
    moving = handle_movement(keys, idle_img)  # Passando idle_img para handle_movement
    current_img = update_animation(dt, moving, walk_imgs, idle_img)
    screen.blit(current_img, (player_x, player_y))
