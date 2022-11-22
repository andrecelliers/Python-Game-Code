#!/usr/bin/python3
### https://www.youtube.com/watch?v=B6DrRN5z_uU 
### left off 22:35
### importing required modules ###
import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join
pygame.init()

### Sets caption at top of the window ###
pygame.display.set_caption("Andre's Platformer")

### Global Variables ###
WIDTH =  1000
HEIGHT = 800
FPS = 60
PLAYER_VEL = 5

### Setting up Pygame Window ### 
window = pygame.display.set_mode((WIDTH, HEIGHT))

### Creating player ### 
class Player(pygame.sprite.Sprite):
    COLOR = (255,0,0)

    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x,y,width,height)
        self.y_vel = 0
    

### Setting up Background function ### 
def get_background(name):
    image =  pygame.image.load(join("assets", "Background", name))
    _, _, width, height = image.get_rect()
    tiles = []

    for i in range(WIDTH // width + 1):
        for j in range(HEIGHT // height +1):
            pos = (i * width, j * height)
            tiles.append(pos)

    return tiles, image

#def draw window
def draw(window,background, bg_image):
    for tile in background:
        window.blit(bg_image, tile)
    pygame.display.update()


#Setting up main function
def main (window):
    clock = pygame.time.Clock()
    background, bg_image = get_background("Brown.png")

    #Define a while loop that runs as event loop
    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        draw(window, background, bg_image) 


    pygame.quit()
    quit()


#Only call main function when running file directly 
if __name__ == "__main__":
    main(window)


