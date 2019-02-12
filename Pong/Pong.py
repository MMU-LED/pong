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
    pygame.font.init()
    #display
    scale = 6#1 for led screen, 6-ish for testing
    height = 80*scale
    width = 96*scale 
    player1_points = 0
    player2_points = 0
    screensize = (height, width)
    twoPlayer = False
    myFont = pygame.font.SysFont("monospace", 10*scale)

  
    #create a new 'screen'/drawing surface - 300x300 resolution 
    #in pygame you have to create a 'surface' and then draw stuff on that surface similar to processing
    #you can have multiple surfaces on screen at once I think - think different menus in a game
    screen = pygame.display.set_mode((screensize))
   
    #limit and track FPS
    clock = pygame.time.Clock()
    
    ball = Ball(screensize, scale)
    player_paddle = Paddle(screensize, screensize[0]-(2*scale), scale)
    player_paddle.color = 255,100,100 # red player
    player2_paddle = Paddle(screensize, 2*scale, scale)

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

            # keyboard input for paddle 2 
            #SACRIFICIAL FEATURE - how does twoPlayer true become false again without the game ending?
            if event.type == KEYDOWN:
                if event.key == K_w:
                    twoPlayer = True    # p2 takes control
                    player2_paddle.color = 100,100,255 # paddle turns blue
                    player2_paddle.direction = -1
                elif event.key == K_s:
                    twoPlayer = True    # P2 takes control
                    player2_paddle.color = 100,100,255 # paddle turns blue
                    player2_paddle.direction = 1
            # when no button is pressed , paddle 2 stops moving
            if event.type == KEYUP:
                if event.key == K_w and player2_paddle.direction == -1:
                    player2_paddle.direction = 0
                elif event.key == K_s and player2_paddle.direction == 1:
                    player2_paddle.direction = 0

              
#####object updating phase
        
        player_paddle.update()
        player2_paddle.update()
        ball.update(player_paddle, player2_paddle, scale)

        # very basic singleplayer - p2 moves on own until input takes over
        if twoPlayer == False: #ai below here
            if  ball.centery > player2_paddle.centery:
                player2_paddle.centery += int (1*scale)/2
            if  ball.centery < player2_paddle.centery:
                player2_paddle.centery -= int (1*scale)/2
           


        if ball.hit_edge_left:
            print ('One point for Player 1!')
            player1_points += 1
            print (player1_points)
            ball = None
            player_paddle = None
            player2_paddle = None
            ball = Ball(screensize, scale)
            player_paddle = Paddle(screensize, screensize[0]-(2*scale), scale)
            player_paddle.color = 255,100,100 # red player
            player2_paddle = Paddle(screensize, 2*scale, scale)
            if player1_points == 2:
                print ('Player 1 wins!')
                player1_points = 0
                player2_points = 0
            #running = False
        elif ball.hit_edge_right:
            print ('One point for Player 2!')
            player2_points += 1
            print (player2_points)
            ball = None
            player_paddle = None
            player2_paddle = None
            ball = Ball(screensize, scale)
            player_paddle = Paddle(screensize, screensize[0]-(2*scale), scale)
            player_paddle.color = 255,100,100 # red player
            player2_paddle = Paddle(screensize, 2*scale, scale)
            if player2_points == 2:
                print ('Player 2 wins')
                player1_points = 0
                player2_points = 0
            #running = False

#####rendering phase

        #Black screen for background
        screen.fill((0,0,0))   

       
        #render text
        label = myFont.render(str(player2_points) ,True, (100,100,100))
        screen.blit(label, (320, 50))
        player_paddle.render(screen, scale)
        player2_paddle.render(screen, scale)
        ball.render(screen, scale)
        #pygame uses 2 screens , so i think it renders 1 frame ahead ( not entirely sure )
        pygame.display.flip() 
        #update display - think void draw from processing
        pygame.display.update()
    pygame.quit()
main()
