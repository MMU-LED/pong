#main - so far this is just a placeholder 
#the paddle and ball classes need to be used in here
#background needs creating
#message needs adding
#etc etc
#remember python does nesting by indentation, not by curly brackets :) 
#~josh 21/01/19

#created a main
#updated the ball class to add collisions wth border of screen and winning conditions when hit either side of screen
#created paddle class with player input ( up/down arrows) and collide with ball
#-Aaron 30/01/2019

from Ball import Ball

from Paddle import Paddle

import pygame, sys 
#import pygame & sys - sys lets us exit the game

from pygame.locals import *
#useful imports - not fully sure what they're for though



def main():
    pygame.init() 
    #display
    scale = 1
    height = 600*scale
    width = 300*scale 
    screensize = (height, width)

    #create a new 'screen'/drawing surface - 300x300 resolution 
    #in pygame you have to create a 'surface' and then draw stuff on that surface similar to processing
    #you can have multiple surfaces on screen at once I think - think different menus in a game
    screen = pygame.display.set_mode((screensize))
   
    #limit and track FPS
    clock = pygame.time.Clock()
    
    ball = Ball(screensize)
    player_paddle = Paddle(screensize, screensize[0]-15)
    player2_paddle = Paddle(screensize, 15)

    # Window Title
    pygame.display.set_caption('MMUARCADE2018')
  
    #this is like void draw 
    #loop below forever
    running = True 
    while running: 
        
        #fps limiting/reporting phase
        clock.tick(64) 
        
#####event handling phase

        #get user events like keypresses
        for event in pygame.event.get():          
            if event.type == QUIT:                      
                running = False;

            # keyboard input for paddle
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    player_paddle.direction = -1
                elif event.key == K_DOWN:
                    player_paddle.direction = 1
            # when no button is pressed , paddle stops moving
            if event.type == KEYUP:
                if event.key == K_UP and player_paddle.direction == -1:
                    player_paddle.direction = 0
                elif event.key == K_DOWN and player_paddle.direction == 1:
                    player_paddle.direction = 0

                    # keyboard input for paddle
            if event.type == KEYDOWN:
                if event.key == K_w:
                    player2_paddle.direction = -1
                elif event.key == K_s:
                    player2_paddle.direction = 1
            # when no button is pressed , paddle stops moving
            if event.type == KEYUP:
                if event.key == K_w and player2_paddle.direction == -1:
                    player2_paddle.direction = 0
                elif event.key == K_s and player2_paddle.direction == 1:
                    player2_paddle.direction = 0

              
#####object updating phase
        
        player_paddle.update()
        player2_paddle.update()
        ball.update(player_paddle, player2_paddle)
        

        if ball.hit_edge_left:
            print ('Player 2 wins!')
            running = False
        elif ball.hit_edge_right:
            print ('Player 1 wins!')
            running = False

#####rendering phase

        #Black screen for background
        screen.fill((0,0,0))   
        
        player_paddle.render(screen)
        player2_paddle.render(screen)
        ball.render(screen)
        #pygame uses 2 screens , so i think it renders 1 frame ahead ( not entirely sure )
        pygame.display.flip() 
        #update display - think void draw from processing
        pygame.display.update()
    pygame.quit()
main()
