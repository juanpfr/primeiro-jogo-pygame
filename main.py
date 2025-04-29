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
    if keys[pygame.K_w]:
        player_y -= player_speed # Move para cima

    if keys[pygame.K_a]:
        player_x -= player_speed # Move para a esquerda

    if keys[pygame.K_s]:
        player_y += player_speed # Move para baixo

    if keys[pygame.K_d]:
        player_x += player_speed # Move para a direita

    # Atualizar tela
    screen.fill(white)                                                                  # Fundo
    pygame.draw.rect(screen, blue, (player_x, player_y, player_size, player_size))      # Desenha o player
    pygame.display.flip()                                                               # Atualiza a tela