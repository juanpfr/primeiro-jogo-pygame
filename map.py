import pygame

# Função para carregar o mapa
def load_map(floor_img, wall_img):
    map_layout = [
        "WWWWWWWWWWWWWWWW",
        "W..............W",
        "W....WWW.......W",
        "W..............W",
        "W....W.........W",
        "W..............W",
        "W.........W....W",
        "W..............W",
        "W......WWWW....W",
        "W....W.........W",
        "W..............W",
        "WWWWWWWWWWWWWWWW",
    ]

    tiles_to_draw = []
    wall_rects = []

    for y, row in enumerate(map_layout):
        for x, tile in enumerate(row):
            if tile == 'W':  # Se for parede, desenha a parede
                wall_rects.append(pygame.Rect(x * 64, y * 64, 64, 64))  # Adiciona a parede para colisão
                tiles_to_draw.append((wall_img, (x * 64, y * 64)))  # Desenha a parede
            elif tile == '.':  # Se for chão, desenha o chão
                tiles_to_draw.append((floor_img, (x * 64, y * 64)))

    return wall_rects, tiles_to_draw
