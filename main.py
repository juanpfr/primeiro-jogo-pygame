# Arquivo principal do projeto

# Importar bibliotecas
import pygame
import sys              # Funcionalidades do sistema

# Preparar o pygame para ser utilizado
pygame.init()

# Tamanho da janela
width = 800
height = 600

# Criar a tela do jogo
screen = pygame.display.set_mode((width, height))

# Título da janela
pygame.display.set_caption("Horror 2D")

# Cores
white = (255, 255, 255)
blue = (0, 0, 255)

# Player
player_x = 100
player_y = 100
player_size = 50
player_speed = 1

# Loop principal (Loop infinito para manter o jogo em execução)
while True:
    # Tratar eventos, clicks ou pressionamento de teclas
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Pegar teclas pressionadas
    keys = pygame.key.get_pressed()

    # Movimentação do player
    if keys[pygame.K_w] and player_y > 0:
        player_y -= player_speed # Move para cima se a posição y for maior que 0

    if keys[pygame.K_a] and player_x > 0:
        player_x -= player_speed # Move para a esquerda se a posição x for maior de 0

    if keys[pygame.K_s] and player_y < height - player_size:
        player_y += player_speed # Move para baixo se a posição y for menor que a altura menos o tamanho do player

    if keys[pygame.K_d] and player_x < width - player_size:
        player_x += player_speed # Move para a direita se a posição x for menor que a largura menos o tamanho do player

    # Atualizar tela
    screen.fill(white)                                                                  # Fundo
    pygame.draw.rect(screen, blue, (player_x, player_y, player_size, player_size))      # Desenha o player
    pygame.display.flip()                                                               # Atualiza a tela