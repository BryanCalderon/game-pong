from Ball import Ball
from Pala import Pala
from Utils import *


def start(screen):
    background_image = load_image('images/fondo.png')
    ball = Ball()
    pala_jud = Pala(30)
    pala_cpu = Pala(WIDTH - 30)
    clock = pygame.time.Clock()
    puntos = [0, 0]
    is_pause = False

    while True:
        time = clock.tick(60)
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    is_pause = True
                if event.key == pygame.K_c:
                    is_pause = False

        if not is_pause:
            puntos = ball.update(time, pala_jud, pala_cpu, puntos)
            pala_jud.mover(time, keys)
            # pala_jud.ia_jug(time, ball)
            pala_cpu.ia(time, ball)

        p_jug, p_jug_rect = get_text(str(puntos[0]), WIDTH / 4, 40)
        p_cpu, p_cpu_rect = get_text(str(puntos[1]), WIDTH - WIDTH / 4, 40)

        screen.blit(background_image, (0, 0))
        screen.blit(p_jug, p_jug_rect)
        screen.blit(p_cpu, p_cpu_rect)
        screen.blit(ball.image, ball.rect)
        screen.blit(pala_jud.image, pala_jud.rect)
        screen.blit(pala_cpu.image, pala_cpu.rect)

        if is_pause:
            text_pause, text_pause_rect = get_text("PAUSE", WIDTH / 2, HEIGHT / 2)
            screen.blit(text_pause, text_pause_rect)

        pygame.display.flip()
