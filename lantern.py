import pygame

def draw_lantern(player_x, player_y, radius, screen, width, height):
    # Criar uma superfície preta que cobre toda a tela
    dark_surface = pygame.Surface((width, height))
    dark_surface.fill((0, 0, 0))

    # Criar uma máscara que irá "iluminar" a área ao redor do jogador
    mask_surface = pygame.Surface((width, height), pygame.SRCALPHA)
    pygame.draw.circle(mask_surface, (0, 0, 0, 0), (player_x, player_y), radius)
    dark_surface.blit(mask_surface, (0, 0), special_flags=pygame.BLEND_RGBA_SUB)

    # Desenhar a superfície escura com a área iluminada
    screen.blit(dark_surface, (0, 0))
