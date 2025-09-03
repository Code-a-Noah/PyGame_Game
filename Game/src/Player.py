import pygame

#from MAIN import (Gravity, Jump_Strength)
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

    def handle_input(self): #Also handles animations the correspond to movement
        now = pygame.time.get_ticks()

        #move the sprite + adding direction specific animations
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.velocity
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.velocity
        if keys[pygame.K_UP]:
            self.velocity_y = Jump_Strength

        def update(self):
            pass