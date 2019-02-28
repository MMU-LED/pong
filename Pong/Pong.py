from Ball import Ball

from Paddle import Paddle

import pygame, sys 
#import pygame & sys - sys lets us exit the game

from pygame.locals import *
#useful imports - not fully sure what they're for though

player1_points = 0
player2_points = 0
p1Control = False   #represents wether paddle is controlled by a player
p2Control = False
screensize = (0,0)
player1_paddle = None
player2_paddle = None
ball = None
screen = None

# Read only
scale = 6 # 1 for led screen, 6-ish for testing
height = 80*scale
width = 96*scale 

def main():
    global player1_points
    global player2_points
    global screensize
    global p1Control
    global p2Control
    global ball
    global screen
    global player1_paddle
    global player2_paddle


    # Initialise PyGame and create screen object
    pygame.init() 
    pygame.font.init()
    screensize = (height, width)
    myFont = pygame.font.SysFont("monospace", 10*scale)
    screen = pygame.display.set_mode((screensize))
    pygame.display.set_caption('MMUARCADE2018')
   
    # limit and track FPS
    clock = pygame.time.Clock()
    
    # Create Ball and paddles
    ball = Ball(screensize, scale)
    player1_paddle = Paddle(screensize, screensize[0]-(2*scale), scale)
    player2_paddle = Paddle(screensize, 2*scale, scale)

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
                    p1Control = True    # p1 takes control
                    player1_paddle.color = 255,100,100 # paddle turns red
                    player1_paddle.direction = -1
                elif event.key == K_DOWN:
                    p1Control = True    # p1 takes control
                    player1_paddle.color = 255,100,100 # paddle turns red
                    player1_paddle.direction = 1
            # when no button is pressed , paddle stops moving
            if event.type == KEYUP:
                if event.key == K_UP and player1_paddle.direction == -1:
                    player1_paddle.direction = 0
                elif event.key == K_DOWN and player1_paddle.direction == 1:
                    player1_paddle.direction = 0

            # keyboard input for paddle 2 
            #SACRIFICIAL FEATURE - A way for paddles switch to AI without game ending?
            if event.type == KEYDOWN:
                if event.key == K_w:
                    p2Control = True    # p2 takes control
                    player2_paddle.color = 100,100,255 # paddle turns blue
                    player2_paddle.direction = -1
                elif event.key == K_s:
                    p2Control = True    # P2 takes control
                    player2_paddle.color = 100,100,255 # paddle turns blue
                    player2_paddle.direction = 1
            # when no button is pressed , paddle 2 stops moving
            if event.type == KEYUP:
                if event.key == K_w and player2_paddle.direction == -1:
                    player2_paddle.direction = 0
                elif event.key == K_s and player2_paddle.direction == 1:
                    player2_paddle.direction = 0

              
#####object updating phase
        
        player1_paddle.update()
        player2_paddle.update()
        ball.update(player1_paddle, player2_paddle, scale)

        # very basic singleplayer - p2 moves on own until input takes over
        if p2Control == False: #ai below here
            if  ball.centery > player2_paddle.centery:
                player2_paddle.centery += int (1*scale)/2
            if  ball.centery < player2_paddle.centery:
                player2_paddle.centery -= int (1*scale)/2
        
        if p1Control == False: #ai below here
            if  ball.centery > player1_paddle.centery:
                player1_paddle.centery += int (1*scale)/2
            if  ball.centery < player1_paddle.centery:
                player1_paddle.centery -= int (1*scale)/2


        if ball.hit_edge_left:
            pointScored("left")
        elif ball.hit_edge_right:
            pointScored("right")

#####rendering phase

        #Black screen for background
        screen.fill((0,0,0))   

       
        #render text
        label = myFont.render(str(player2_points) ,True, (100,100,100))
        screen.blit(label, (320, 50))
        player1_paddle.render(screen, scale)
        player2_paddle.render(screen, scale)
        ball.render(screen, scale)
        #pygame uses 2 screens , so i think it renders 1 frame ahead ( not entirely sure )
        pygame.display.flip() 
        #update display - think void draw from processing
        pygame.display.update()
    pygame.quit()

def keyboardHandler():
    print("Placeholder")

def paddleHandler():
    print("Placeholder")

def pointScored(side):
    global player1_points
    global player2_points
    global screensize
    global p1Control
    global p2Control
    global ball
    global screen
    global player1_paddle
    global player2_paddle

    if side == "left":
        # ball has gone left
        print("One point for Player 1!")
        player1_points += 1
        print (player1_points)
        
    elif side == "right":
        # ball has gone right
        print ('One point for Player 2!')
        player2_points += 1
        print (player2_points)
    
    # reset ball
    ball = Ball(screensize, scale)
    # paddles no longer reset here - readd if necessary
    
    if p1Control == True:
        player1_paddle.color = 255,100,100 # red player
    if p2Control == True:
        player2_paddle.color = 100,100,255 # blue player
    
    if player1_points == 2:
        print ('Player 1 wins!')
        resetGame()
    if player2_points == 2:
        print ('Player 2 wins')
        resetGame()


def resetGame():
    global player1_points
    global player2_points
    global screensize
    global p1Control
    global p2Control
    global ball
    global screen
    global player1_paddle
    global player2_paddle

    wprint("Game Reset")
    player1_points = 0
    player2_points = 0
    p1Control = False
    p2Control = False
    player1_paddle = Paddle(screensize, screensize[0]-(2*scale), scale)
    player2_paddle = Paddle(screensize, 2*scale, scale)

    # Reset Stuff
main()
