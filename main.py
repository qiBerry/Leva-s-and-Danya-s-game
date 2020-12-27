import pygame
import os

#asset folder init
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'textures')
player_img = pygame.image.load(os.path.join(img_folder, 'cloud.png'))

#game init
WIDTH = 360  # screen width
HEIGHT = 480 # screen height
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
    def update(self):
        self.rect.x += 2
        if self.rect.left > WIDTH:
            self.rect.right = 0
            
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)


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
    
