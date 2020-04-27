from Utils import load_image, pygame, WIDTH, HEIGHT


class Pala(pygame.sprite.Sprite):
    def __init__(self, x):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("images/pala.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = HEIGHT / 2
        self.speed = 0.5

    def mover(self, time, keys):
        if self.rect.top >= 0:
            if keys[pygame.K_UP]:
                self.rect.centery -= self.speed * time
        if self.rect.bottom <= HEIGHT:
            if keys[pygame.K_DOWN]:
                self.rect.centery += self.speed * time

    def ia(self, time, ball):
        if ball.speed[0] >= 0 and ball.rect.centerx > (WIDTH * 2) / 3:
            if self.rect.centery < ball.rect.centery:
                self.rect.centery += self.speed * time
            if self.rect.centery > ball.rect.centery:
                self.rect.centery -= self.speed * time

    def ia_jug(self, time, ball):
        if ball.speed[0] <= 0 and ball.rect.centerx <= WIDTH / 2:
            if self.rect.centery < ball.rect.centery:
                self.rect.centery += self.speed * time
            if self.rect.centery > ball.rect.centery:
                self.rect.centery -= self.speed * time
