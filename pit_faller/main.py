import pygame
import random

pygame.init()

width = 500
height = 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ant Dodger")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

ant_img = pygame.image.load("ant.png")
raindrop_img = pygame.image.load("raindrop.png")

class Ant(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = ant_img
        self.rect = self.image.get_rect()
        self.rect.centerx = width / 2
        self.rect.bottom = height - 10
        self.speed = 0

    def update(self):
        self.speed = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.speed = -5
        if keys[pygame.K_RIGHT]:
            self.speed = 5
        self.rect.x += self.speed
        if self.rect.right > width:
            self.rect.right = width
        if self.rect.left < 0:
            self.rect.left = 0

    def draw(self):
        screen.blit(self.image, self.rect)


class Raindrop(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = raindrop_img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, width - self.rect.width)
        self.rect.y = -self.rect.height
        self.speed = random.randint(3, 7)

    def update(self):
        self.rect.y += self.speed

    def draw(self):
        screen.blit(self.image, self.rect)


all_sprites = pygame.sprite.Group()
ants = pygame.sprite.Group()
raindrops = pygame.sprite.Group()

ant = Ant()
all_sprites.add(ant)
ants.add(ant)

clock = pygame.time.Clock()
score = 0

font = pygame.font.Font(None, 36)
score_text = font.render("Score: {}".format(score), True, WHITE)
score_rect = score_text.get_rect()
score_rect.topright = (width - 10, 10)

running = True
game_over = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        all_sprites.update()

        hits = pygame.sprite.spritecollide(ant, raindrops, False, pygame.sprite.collide_rect_ratio(0.7))
        if hits:
            game_over = True

        if random.randint(0, 100) < 10:
            raindrop = Raindrop()
            all_sprites.add(raindrop)
            raindrops.add(raindrop)

    screen.fill(BLACK)

    all_sprites.draw(screen)

    if game_over:
        text = font.render("Game Over! Your Score: {}".format(score), True, RED)
        text_rect = text.get_rect()
        text_rect.centerx = screen.get_rect().centerx
        text_rect.centery = screen.get_rect().centery
        screen.blit(text, text_rect)
    else:
        score += 1
        score_text = font.render("Score: {}".format(score), True, WHITE)
        screen.blit(score_text, score_rect)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
