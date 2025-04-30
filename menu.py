# Configuração de Menu

import pygame
from main import screen

font = pygame.font.SysFont("arialblack", 40)

# Definir cores
text_color = (255, 255, 255)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_color)
    screen.blit(img, (x, y))