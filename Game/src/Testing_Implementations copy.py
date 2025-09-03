import pygame
import sys

#initialize pygame
pygame.init()

#Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Blobby Bobby")

tile_set = pygame.image.load('Game/Assets/Images/Tile Sets/TileSet1.png')

TILE_SIZE = 60

tile_map = [
     [],
     [],
     [],
     [1],
     [0, 1],
     [0, 0, 1, 0, 0, 4, 2, 2, 2, 3, 0, 1],
     [0, 0, 0, 1],
     [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
     [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
     [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
]
def draw_tile_map(screen, tile_map, tile_set, tile_size):
     for y, row in enumerate(tile_map):
          for x, tile in enumerate(row):
               tile_rect = pygame.Rect(tile * tile_size, 0, tile_size, tile_size)
               screen.blit(tile_set, (x * tile_size, y * tile_size), tile_rect)
#Function to load images into the convert_alpha()
def loadify(imgname):
        return pygame.image.load(imgname).convert_alpha()
#Background
background = loadify('Game/Assets/Images/Background.png')

#setup clock
clock = pygame.time.Clock()





   
        
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
    screen.blit(background, (0,0))
    draw_tile_map(screen, tile_map, tile_set, TILE_SIZE)

    
    #Update display
    pygame.display.flip()

    #Cap framerate
    clock.tick(60)


#Quit pygame
pygame.quit()
sys.exit()