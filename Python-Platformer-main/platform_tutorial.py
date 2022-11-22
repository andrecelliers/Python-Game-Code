#/usr/bin/python3

### importing required modules ###
import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join
pygame.init()

### Sets caption at top of the window ###
pygame.display.set_caption("Platformer")

### Global Variables ###
BG_COLOR = (255,255,255)
WIDTH =  1000
HEIGHT = 800
FPS = 60
PLAYER_VEL = 5

#Setting up Pygame Window
window = pygame.display.set_mode((WIDTH, HEIGHT))

#Setting up main function
def main (window):
    clock = pygame.time.Clock()

    #Define a while loop that runs as event loop
    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()
    quit()


#Only call main function when running file directly 
if __name__ == "__main__":
    main(window)


