import pygame
import random

pygame.init()  # inicia o pygame

# tamanho da janela do jogo
x = 1920
y = 1080

# abrir a janela
screen = pygame.display.set_mode((x, y))
pygame.display.set_caption('My first game in Python')

# carrega e define o tamanho da imagem de fundo
bg = pygame.image.load('img/tela.jpg')
bg = pygame.transform.scale(bg, (x, y))

# imagem do inimigo
inimigo = pygame.image.load('img/inimigo.png').convert_alpha()
inimigo = pygame.transform.scale(inimigo, (55, 55))

# imagem do player
playerImg = pygame.image.load('img/player.png').convert_alpha()
playerImg = pygame.transform.scale(playerImg, (65, 65))
playerImg = pygame.transform.rotate(playerImg, -90)

# imagem do golpe
golpe = pygame.image.load('img/golpe.png').convert_alpha()
golpe = pygame.transform.scale(golpe, (30, 30))
golpe = pygame.transform.rotate(golpe, 0)

# posições
pos_inimigo_x = 500
pos_inimigo_y = 500

pos_player_x = 200
pos_player_y = 500

vel_x_golpe = 0
pos_x_golpe = 200
pos_y_golpe = 500

# pontuação e nível
pontos = 3
nivel = 1
vel_inimigo = 1  # começa lento
vel_jogador = 4  # velocidade inicial do jogador

triggered = False
rodando = True

font = pygame.font.SysFont('font/PixelGameFont.ttf', 50)

# objeto da imagem
player_rect = playerImg.get_rect()
inimigo_rect = inimigo.get_rect()
golpe_rect = golpe.get_rect()


# funções
def respawn():
    x = 1950
    y = random.randint(1, y - 80)  # limite vertical ajustado
    return [x, y]


def respawn_golpe():
    triggered = False
    respawn_golpe_x = pos_player_x
    respawn_golpe_y = pos_player_y
    vel_x_golpe = 0
    return [respawn_golpe_x, respawn_golpe_y, triggered, vel_x_golpe]


def colisions():
    global pontos
    if player_rect.colliderect(inimigo_rect) or inimigo_rect.x <= 60:
        pontos -= 1
        return True
    elif golpe_rect.colliderect(inimigo_rect):
        pontos += 1
        return True
    else:
        return False


# loop principal
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    # atualizar nível e velocidades
    if pontos >= 50:
        nivel = 4
    elif pontos >= 30:
        nivel = 3
    elif pontos >= 10:
        nivel = 2
    else:
        nivel = 1

    vel_inimigo = nivel  # inimigo fica mais rápido conforme o nível
    vel_jogador = 4 + (nivel - 1)  # jogador também mais rápido
    golpe_vel_base = 1.5 + (nivel - 1) * 0.5  # golpe mais rápido

    # teclas
    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_UP] and pos_player_y > 1:
        pos_player_y -= vel_jogador
        if not triggered:
            pos_y_golpe -= vel_jogador

    if tecla[pygame.K_DOWN] and pos_player_y < (y - 65):  # limite de altura
        pos_player_y += vel_jogador
        if not triggered:
            pos_y_golpe += vel_jogador

    if tecla[pygame.K_w] and pos_player_y > 1:
        pos_player_y -= vel_jogador
        if not triggered:
            pos_y_golpe -= vel_jogador

    if tecla[pygame.K_s] and pos_player_y < (y - 65):
        pos_player_y += vel_jogador
        if not triggered:
            pos_y_golpe += vel_jogador

    if tecla[pygame.K_SPACE]:
        triggered = True
        vel_x_golpe = golpe_vel_base

    if pontos == -1:
        rodando = False

    # respawn inimigo
    if pos_inimigo_x <= 50:
        pos_inimigo_x, pos_inimigo_y = respawn()

    # respawn golpe
    if pos_x_golpe >= 1950:
        pos_x_golpe, pos_y_golpe, triggered, vel_x_golpe = respawn_golpe()

    # colisões
    if colisions():
        pos_inimigo_x, pos_inimigo_y = respawn()

    # posição do rect
    player_rect.y = pos_player_y
    player_rect.x = pos_player_x

    golpe_rect.y = pos_y_golpe
    golpe_rect.x = pos_x_golpe

    inimigo_rect.y = pos_inimigo_y
    inimigo_rect.x = pos_inimigo_x

    # movimento
    pos_inimigo_x -= vel_inimigo
    pos_x_golpe += vel_x_golpe

    # desenhar fundo
    screen.blit(bg, (0, 0))

    # desenhar pontuação e nível
    score = font.render(f'Pontos: {int(pontos)}', True, (255, 255, 255))
    level_text = font.render(f'Nível: {nivel}', True, (255, 255, 0))
    screen.blit(score, (50, 50))
    screen.blit(level_text, (50, 110))

    # desenhar imagens
    screen.blit(inimigo, (pos_inimigo_x, pos_inimigo_y))
    screen.blit(golpe, (pos_x_golpe, pos_y_golpe))
    screen.blit(playerImg, (pos_player_x, pos_player_y))

    pygame.display.update()
