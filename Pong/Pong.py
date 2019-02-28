from Ball import Ball

from Paddle import Paddle

import pygame, sys 
#import pygame & sys - sys lets us exit the game

from pygame.locals import *
#useful imports

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
scale = 8 # 1 for led screen, 6-ish for testing
height = 80*scale
width = 96*scale 
scoreLimit = 2
keyboardControl = True

# Global Keyword needed if want to write to global variable (Not if only reading)

# MAIN - START OF MAIN CODE
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
    global scoreLimit
    global myFont

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

    running = True 
    while running:  # MAIN LOOP

        # FRAME SPEED LIMIT
        clock.tick(64) 
        # EVENT HANDLING
        for event in pygame.event.get():          
            if event.type == QUIT:                      
                running = False;
            elif keyboardControl == True:
                keyboardHandler(event)      # KEYBOARD CONTROLS
        if keyboardControl == False:
            groveControlsHandler()          # GROVE CONTROLS
              
        # OBJECT UPDATING
        player1_paddle.update()
        player2_paddle.update()
        ball.update(player1_paddle, player2_paddle, scale)

        # AI CONTROLS
        if p2Control == False: 
            paddleAI(player2_paddle)
        if p1Control == False:
            paddleAI(player1_paddle)

        # POINT SCORING
        if ball.hit_edge_left:
            pointScored("left")
        elif ball.hit_edge_right:
            pointScored("right")

        # RENDER - SEE BELOW
        render() 
    pygame.quit()  # executes when "running" is set to False


# RENDER - CONTAINS USED TO DRAW OBJECTS TO THE SCREEN
def render():
    global screen 
    screen.fill((0,0,0))   # Black screen for background
    
    # RENDER TEXT
    label = myFont.render(str(player2_points) ,True, (100,100,100)) 
    screen.blit(label, (320, 50))
    player1_paddle.render(screen, scale)
    player2_paddle.render(screen, scale)
    ball.render(screen, scale)
    pygame.display.flip()   # pygame uses 2 screens , so i think it renders 1 frame ahead ( not entirely sure )
    pygame.display.update() # Update Display


# AI - MOVE PADDLE TOWARDS BALL
def paddleAI(AI_paddle):
    global ball
    if  ball.centery > AI_paddle.centery:
        AI_paddle.centery += int (1*scale)/2
    if  ball.centery < AI_paddle.centery:
        AI_paddle.centery -= int (1*scale)/2


# KEYBOARD - MOVE PADDLES WITH KEY CONTROLS
def keyboardHandler(event):
    global p1Control
    global p2Control
    global player1_paddle
    global player2_paddle
    
    # KEY PRESSED EVENT
    if event.type == KEYDOWN:
        if event.key == K_UP:
            p1Control = True
            player1_paddle.color = 255,100,100
            player1_paddle.direction = -1
        elif event.key == K_DOWN:
            p1Control = True
            player1_paddle.color = 255,100,100 
            player1_paddle.direction = 1

        if event.key == K_w:
            p2Control = True    
            player2_paddle.color = 100,100,255 
            player2_paddle.direction = -1
        elif event.key == K_s:
            p2Control = True
            player2_paddle.color = 100,100,255
            player2_paddle.direction = 1

    # KEY RELEASED EVENT
    if event.type == KEYUP:
        if event.key == K_UP and player1_paddle.direction == -1:
            player1_paddle.direction = 0
        elif event.key == K_DOWN and player1_paddle.direction == 1:
            player1_paddle.direction = 0

        if event.key == K_w and player2_paddle.direction == -1:
            player2_paddle.direction = 0
        elif event.key == K_s and player2_paddle.direction == 1:
            player2_paddle.direction = 0


# GROVE CONTROLS - GET VALUE FROM ROTARY SENSORS AND CONVERT TO PADDLE CO-OORD
# NOT YET IMPLEMENTED
def groveControlsHandler():
    print("Placeholder")


# POINT SCORED - TRACK SCORE AND CHECK IF GAME IS OVER YET
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
    global scoreLimit

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
    
    if player1_points == scoreLimit:
        print ('Player 1 wins!')
        resetGame()
    if player2_points == scoreLimit:
        print ('Player 2 wins')
        resetGame()


# RESET - RETURN GAME TO DEFAULT STATE AFTER GAME HAS ENDED
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

    print("Game Reset")
    player1_points = 0
    player2_points = 0
    p1Control = False
    p2Control = False
    player1_paddle = Paddle(screensize, screensize[0]-(2*scale), scale)
    player2_paddle = Paddle(screensize, 2*scale, scale)

# RUN THE GAME
main()
