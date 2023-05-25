from settings import *
import pygame
import sprites
import game_over

player_one = False

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
        self.velocity = pygame.math.Vector2(0, 0)
        self.gravity = pygame.math.Vector2(0, PLAYER_GRAVITY)
        

    def update(self):
        self.velocity += self.gravity
        self.rect.move_ip(self.velocity.x, self.velocity.y)
        
        # Check collision with platforms
        if pygame.sprite.spritecollide(self, sprites.platforms, False):
            self.rect.y -= self.velocity.y
            self.velocity.y = 0
            self.state = "resting"

        # Check collision with ground
        if self.rect.bottom >= WINDOW_HEIGHT + 250:
            game_over.trigger_game_over()

    def jump(self):
        tolerance = 15
        self.rect.y += tolerance  # Move player down slightly to check collision below
        platforms_collided = pygame.sprite.spritecollide(self, sprites.platforms, False)
        self.rect.y -= tolerance  # Move player back up
        
        if platforms_collided:
            self.velocity.y = -PLAYER_JUMP_HEIGHT

def start():
  global player_one
  player_one = Player()
  sprites.player.add(player_one)

def update():
  global player_one
  player_one.update()

def jump():
  global player_one
  player_one.jump()