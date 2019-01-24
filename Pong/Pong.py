#main - so far this is just a placeholder 
#the paddle and ball classes need to be used in here
#background needs creating
#message needs adding
#etc etc
#remember python does nesting by indentation, not by curly brackets :) 
#~josh 21/01/19
from Ball import Ball

import pygame, sys 
#import pygame & sys - sys lets us exit the game

from pygame.locals import *
#useful imports - not fully sure what they're for though

pygame.init()
#display

DISPLAY_SURFACE = pygame.display.set_mode((300,300))
#create a new 'screen'/drawing surface - 300x300 resolution 
#in pygame you have to create a 'surface' and then draw stuff on that surface similar to processing
#you can have multiple surfaces on screen at once I think - think different menus in a game

pygame.display.set_caption('MMUARCADE2018')
#display placeholder caption on surface to show this is all actually working

#pygame.draw.circle(DISPLAY_SURFACE, (255,255,0), (50, 50), (10), 5);
myBall = Ball(50, 50, 5, DISPLAY_SURFACE) #variables in ball (and presumably paddle) class not working 
myBall.render()

hello = True 
while hello == True:
    #loop below forever

    for event in pygame.event.get():
        #get user events like keypresses
        if event.type == QUIT:
        #if user wants to quit:
            pygame.quit()
            sys.exit()
            #end game and close window

    #update display - think void draw from processing
    pygame.display.update()
