import pygame
import sys

# Constantes
WIDTH = 640
HEIGHT = 480


# Funciones
# ---------------------------------------------------------------------
def load_image(filename, transparent=False):
    try:
        image = pygame.image.load(filename)
    except pygame.error as message:
        raise SystemExit(message)
    image = image.convert()
    if transparent:
        colors = image.get_at((0, 0))
        image.set_colorkey(colors, pygame.RLEACCEL)
    return image


def get_text(texto, posx, posy, colors=(255, 255, 255)):
    fuente = pygame.font.Font("images/DroidSans.ttf_/DroidSans.ttf", 25)
    salida = pygame.font.Font.render(fuente, texto, 1, colors)
    salida_rect = salida.get_rect()
    salida_rect.centerx = posx
    salida_rect.centery = posy
    return salida, salida_rect


def is_close():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)

# ---------------------------------------------------------------------
