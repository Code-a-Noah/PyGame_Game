import pygame
import sys

#initialize pygame
pygame.init()

#Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Blobby Bobby")

#setup clock
clock = pygame.time.Clock()

#Player Sprite
class Player(pygame.sprite.Sprite):
    def __init__(self, images, pos):
        super().__init__()
        self.images = images
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.last_update = pygame.time.get_ticks()
        self.animation_delay = 100 #miliseconds
        self.velocity = 5
        self.moving = pygame.time.get_ticks()
        self.idle_delay = 10
        self.idle_animation_delay = 500
    
    def update(self):
        now = pygame.time.get_ticks()
        
        #move the sprite + adding direction specific animations
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.velocity
            self.moving = now
            self.images = [pygame.image.load(f'Game/Assets/Images/Player/PlayerRunL_{i}.png') for i in range(4)]
            if now - self.last_update > self.animation_delay:
                self.last_update = now
                self.index += 1
                if self.index >= len(self.images):
                    self.index = 0
                self.image = self.images[self.index]
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.velocity
            self.moving = now
            self.images = [pygame.image.load(f'Game/Assets/Images/Player/PlayerRunR_{i}.png') for i in range(4)]
            if now - self.last_update > self.animation_delay:
                self.last_update = now
                self.index += 1
                if self.index >= len(self.images):
                    self.index = 0
                self.image = self.images[self.index]
        if keys[pygame.K_UP]:
            self.images = [pygame.image.load(f'Game/Assets/Images/Player/PlayerIdle_{i}.png') for i in range(1)]
            self.rect.y -= self.velocity
            self.moving = now
            if now - self.last_update > self.animation_delay:
                self.last_update = now
                self.index += 1
                if self.index >= len(self.images):
                    self.index = 0
                self.image = self.images[self.index]
        if keys[pygame.K_DOWN]:
            self.images = [pygame.image.load(f'Game/Assets/Images/Player/PlayerIdle_{i}.png') for i in range(1)]
            self.moving = now
            self.rect.y += self.velocity
            if now - self.last_update > self.animation_delay:
                self.last_update = now
                self.index += 1
                if self.index >= len(self.images):
                    self.index = 0
                self.image = self.images[self.index]
        #Idle animation
        if now - self.moving > self.idle_delay:
            if len(self.images) != 7:
                self.images = [pygame.image.load(f'Game/Assets/Images/Player/PlayerIdle_{i}.png') for i in range(7)]
                self.index = 0
                self.image = self.images[self.index]
                self.last_update = now
            if now - self.last_update > self.idle_animation_delay:
                self.last_update = now
                self.index += 1
                if self.index >= len(self.images):
                    self.index = 0
                self.image = self.images[self.index]
        #Barrier (So the player cant leave the screen)
        if self.rect.x == 700:
            self.rect.x -= self.velocity
        if self.rect.x == -50:
            self.rect.x += self.velocity
        if self.rect.y == 500:
            self.rect.y -= self.velocity
        if self.rect.y == -50:
            self.rect.y += self.velocity
        
#Starts game with idle animation       
images = [pygame.image.load(f'Game/Assets/Images/Player/PlayerIdle_{i}.png') for i in range(1)]
#initialize sprites
player = Player(images, (100,100))
all_sprites = pygame.sprite.Group(player)

#main game loop
running = True
while running:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if keys[pygame.K_ESCAPE]:
        running = False
    

    #Fill screen
    screen.fill((255,255,255))


    #Update and draw all sprites
    all_sprites.update()
    all_sprites.draw(screen)
    
    #Update display
    pygame.display.flip()

    #Cap framerate
    clock.tick(60)


#Quit pygame
pygame.quit()
sys.exit()