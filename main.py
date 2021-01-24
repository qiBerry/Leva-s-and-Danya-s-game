import pygame
import os
import random

#asset folder init
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'textures')
player_img = pygame.image.load(os.path.join(img_folder, 'player.png'))
enemy_img = pygame.image.load(os.path.join(img_folder, 'enemy.png'))

#game init
WIDTH = 400  # screen width
HEIGHT = 400 # screen height
FPS = 30 # частота кадров в секунду
pygame.init() #game init
pygame.mixer.init() #sound init
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # screen init
pygame.display.set_caption("Leva and Danya")
clock = pygame.time.Clock()

#colors init
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#Sprites init
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2 - 150)
        self.speedx = 0
        self.speed = 8
    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -self.speed
        if keystate[pygame.K_RIGHT]:
            self.speedx = self.speed
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(180, HEIGHT)
        self.speedy = random.randrange(1, 5)
    def update(self):
        self.rect.y -= self.speedy
        if self.rect.bottom < 0:
            self.rect.top = HEIGHT

            
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
for i in range(5):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)


running = True
while running:
    #Update
    clock.tick(FPS)
    all_sprites.update()

    #Events 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #Draw
    screen.fill(BLUE)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
    
