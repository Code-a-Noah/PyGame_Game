import pygame, sys

from Player import *
from Tiles import *

###### SETUP CONSTANTS ######
Gravity = 0.5

###### LOAD UP BASIC WINDOW AND CLOCK ######
pygame.init()
DISPLAY_W, DISPLAY_H = 600, 600
screen = pygame.Surface((DISPLAY_W, DISPLAY_H))
window = pygame.display.set_mode(((DISPLAY_W, DISPLAY_H)))
running = True
clock = pygame.time.Clock()

##### LOAD PLAYER AND SPRITESHEET #####
#all_sprites = pygame.sprite.Group(Player)
player_rect = Player.image.get_rect()
##### LOAD THE LEVEL #####

level_data = load_level_data('Game/src/tilemap.json')
player = create_level(level_data)

##### GAME LOOP #####
while running:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if keys[pygame.K_ESCAPE]:
        running = False
    

    #Fill screen
    screen.fill((0,0,0))


    #Update and draw all sprites
    #all_sprites.update()
    #all_sprites.draw(screen)
    
    #Update display
    pygame.display.flip()

    #Cap framerate
    clock.tick(60)


#Quit pygame
pygame.quit()
sys.exit()

