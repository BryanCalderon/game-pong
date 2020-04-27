#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Módulos
from Utils import load_image, pygame, get_text, is_close, WIDTH, HEIGHT
from game import start


def main():
    # Creamos la ventana pasandole como parametros una tupla con los valores
    # del Alto y ancho definidos para definir las dimensiones de la ventana.
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # Definimos el titulo de la ventana.
    pygame.display.set_caption("Pong Game")
    cover_image = load_image('images/cover.jpg')
    sprite_text, sprite_text_rect = get_text("PRESS ANY BUTTON", WIDTH / 2, (HEIGHT * 6) / 8)

    while True:
        is_close()
        screen.blit(cover_image, (0, 0))
        screen.blit(sprite_text, sprite_text_rect)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                start(screen)
                break

        pygame.display.flip()
    return 0


if __name__ == '__main__':
    pygame.init()
    main()
