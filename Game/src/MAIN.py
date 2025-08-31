import pygame
import sys

#initialize pygame
pygame.init()

#Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Blobby Bobby")

#Setup constants
Gravity = 0.5
Jump_Strength = -10
Ground_level = 500
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
        self.velocity_y = 0
        self.moving = pygame.time.get_ticks()
        self.idle_delay = 10
        self.idle_animation_delay = 500
        self.animation_jump_delay = 40
        self.idle_jump_delay = 1000
        self.was_on_ground = True
        self.landing = False
        self.landing_time = 0
        self.landing_duration = 15
    #Applies gravity
    def apply_gravity(self):
        self.velocity_y += Gravity
        self.rect.y += self.velocity_y
        if self.rect.y > Ground_level:
            self.rect.y = Ground_level
            self.velocity_y = 0
    def handle_input(self): #Also handles animations the correspond to movement
        now = pygame.time.get_ticks()

        #move the sprite + adding direction specific animations
        keys = pygame.key.get_pressed()
        just_landed = not self.was_on_ground and self.on_ground()
        just_jumped = self.was_on_ground and not self.on_ground()
        on_ground = self.on_ground()
        self.was_on_ground = on_ground
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
        if keys[pygame.K_SPACE] and on_ground:
            self.moving = now
            self.velocity_y = Jump_Strength
        if not on_ground:
            self.moving = now
            if just_jumped:
                self.images = [pygame.image.load(f'Game/Assets/Images/Player/PlayerJump_{i}.png') for i in range(5)]
                self.index = 0
                self.image = self.images[self.index]
                self.last_update = now
            if -1 < self.velocity_y < 1:
                self.index = 0
                self.image = self.images[self.index]
                self.images = [pygame.image.load(f'Game/Assets/Images/Player/PlayerJump_0.png')]
            else:
                if now - self.last_update > self.animation_jump_delay:
                    self.last_update = now
                    self.index += 1
                    if self.index >= len(self.images):
                        self.index = 0
                    self.image = self.images[self.index]
        if just_landed:
           self.landing = True
           self.landing_time = now
           self.images = [pygame.image.load(f'Game/Assets/Images/Player/PlayerLand_{i}.png') for i in range(2) ]
           self.index = 0
           self.image = self.images[self.index]
           self.last_update = now
        if self.landing:
            if now - self.last_update > self.animation_delay:
                self.last_update = now
                self.index += 1
                if self.index >= len(self.images):
                    self.index = 0
                self.image = self.images[self.index]
            if now - self.landing_time > self.landing_duration:
                self.landing = False
            return
        #Idle animation
        if now - self.moving > self.idle_delay and on_ground:
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
        if self.rect.y == 600:
            self.rect.y -= self.velocity
        if self.rect.y == -50:
            self.rect.y += self.velocity
         
    def on_ground(self):
        return self.rect.y >= Ground_level
    def update(self):
        self.handle_input()
        self.apply_gravity()
        
    
   
        
#Starts game with idle animation       
images = [pygame.image.load(f'Game/Assets/Images/Player/PlayerIdle_{i}.png') for i in range(1)]
#initialize sprites
player = Player(images, (100,200))
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