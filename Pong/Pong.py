import pygame, sys, time
import config
#import pygame & sys - sys lets us exit the game
from Ball import Ball
from Paddle import Paddle
from pygame.locals import *



try:
    import grovepi # try to import grovepi and setup grove if found
    print("On the pi and have access to grove libraries!")
    keyboardControl = False;
    grovepi.pinMode(config.groveP1, "INPUT")
    grovepi.pinMode(config.groveP2, "INPUT")
    grovepi.pinMode(config.groveButton, "INPUT")
    time.sleep(1)
except ImportError: # there is no grove
    print("Not on the pi, grove disabled!")
    keyboardControl = True;


# get config settings
height = config.height
width = config.width
scale = config.scale
scoreLimit = config.scoreLimit

player1_points = 0
player2_points = 0
p1Control = False   #represents wether paddle is controlled by a player
p2Control = False
screensize = (0,0)
player1_paddle = None
player2_paddle = None
ball = None
screen = None
messageScroll = 0
# Tracking if grove controls have changed
p1Grove_Initial = 0
p2Grove_Initial = 0


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
    global messageScroll 
    # Initialise PyGame and create screen object
    pygame.init() 
    pygame.font.init()
    screensize = (height, width)
    myFont = pygame.font.SysFont("monospace", 8*scale)
    screen = pygame.display.set_mode((screensize))
    pygame.display.set_caption('MMUARCADE2018')

    # set up grove input detection
    groveInitalRead()
   
    # limit and track FPS
    clock = pygame.time.Clock()
    
    # Create Ball and paddles
    ball = Ball(screensize, scale)
    player1_paddle = Paddle(screensize, screensize[0]-(2*scale)-2, scale)
    player2_paddle = Paddle(screensize, 2*scale+2, scale)

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
    global messageScroll
    screen.fill((0,0,0))   # Black screen for background
    
    # RENDER TEXT


    #label = myFont.render(str(player2_points) ,True, (100,100,100))  
    #screen.blit(label, (320, 50))
    messageText = "This is a message1 This is a message2 This is a message3"
    Message = myFont.render(str(messageText) ,True, (100,100,100)) 
    messageScroll += scale *0.5
    screen.blit(Message, ((80 * scale )-messageScroll, -3))
    if messageScroll > len(messageText * scale  * 7):
       messageScroll = 0
    #label = myFont.render(str(len(messageText * scale  * 8)) ,True, (100,100,100))  
    #screen.blit(label, (100, 100))

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


def processRotaryInput(rotary_input):  # Clean Rotary input to 0 - 100
    if rotary_input <= 11.5:
        paddle_coord = 0
    elif rotary_input >= (1023-11.5):
        paddle_coord = 1000
    else:
         paddle_coord = rotary_input
    return int(paddle_coord / 10)



# GROVE CONTROLS - GET VALUE FROM ROTARY SENSORS AND CONVERT TO PADDLE CO-OORD
# NOT YET IMPLEMENTED
def groveControlsHandler():
    global player1_paddle
    global player2_paddle
    try:
        p1_value = processRotaryInput(grovepi.analogRead(config.groveP1))
        p2_value = processRotaryInput(grovepi.analogRead(config.groveP2))

        # Detect input on grove controls
        if (abs(p1_value) - p1Grove_Initial) > config.grove_Threshold:
            p1Control == True
        if (abs(p2_value) - p2Grove_Initial) > config.grove_Threshold:
            p2Control == True

        butt_value = grovepi.digitalRead(config.groveButton)
        print(str(p1_value) + " " + str(p2_value) + " " + str(butt_value))
        # these values are 0 - 100. Need to be converted so that 0 is bottom of the screen and 100 is top
        # maybe percentage of (screensize adjusted for centre of paddle)
        if p1Control == True:
            player1_paddle.centery = (p1_value/100) * (screensize[1]) # may need adjusting
        if p2Control == True:
            player2_paddle.centery = (p2_value/100) * (screensize[1])
    except IOError:
        print("Error Reading grove controls!")


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


def groveInitalRead():
    global p1Grove_Initial
    global p2Grove_Initial
    if keyboardControl == False: ## set inital values
        p1Grove_Initial = processRotaryInput(grovepi.analogRead(config.groveP1))
        p2Grove_Initial = processRotaryInput(grovepi.analogRead(config.groveP2))



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

    groveInitalRead()
    p1Control = False
    p2Control = False
    player1_paddle = Paddle(screensize, screensize[0]-(2*scale)-2, scale)
    player2_paddle = Paddle(screensize, 2*scale+2, scale)

# RUN THE GAME
main()
