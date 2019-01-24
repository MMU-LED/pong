import pygame

class Ball(object):
    """"""
    scale = 10 
    height = 90 * scale
    width = 80 * scale
    x = 0
    y = 0
    ballRadiusX = 5*scale
    ballRadiusY = ballRadiusX 
    topOfBall = y + ballRadiusY
    botOfBall = y - ballRadiusY
    rightOfBall = x + ballRadiusX
    leftOfBall = x - ballRadiusX
    s = 0 #speed :)   
    surface = pygame.display.set_mode((300,300))

    dx = s * scale
    dy = s * scale

    
    def __init__ (self, xinit, yinit, sinit, surface): #initiate class (constructor?)
        self.x = xinit
        self.y = yinit
        self.s = sinit
        self.surface = surface

    def render(surface): #this needs finishing i think - lookup pygame.draw commands 
        pygame.draw.circle(pygame.display.set_mode((300,300)), (255, 0, 0), (50, 50), 5)

    def reset(): #reset ball position to centre of screen - needs changing so resets to near paddle - also needs dx dy values setting
        x = 0 + 1/2 * width
        y = 0 + 1/2 * height 

    def move(): #self explanatory
        x = x + dx
        y = y + dxy
        

    def score(): #if ball exceeds left side of screen, score right = true, if ball exceeds right side, score left = true
        if x + ballRadiusX > width:
            scoreLeft = True
            scoreRight = False
            reset()
        if x - ballRadiusX < 0:
            scoreRight = True
            scoreLeft = False
            reset()


    def edgeDetect ():
        if y + ballRadiusY > height or y - ballRadiusY < 0: 
            dy = - dy 
            
    def bounce(self, Paddle): #self is like 'this' in java 
        #ball reflects off paddle - atm ball going horizontally 
        #this needs changing so the ball comes off at an angle depending on where the ball contacts the paddle
        #along the y axis 
        if self.topOfBall > Paddle.top and self.botOfBall < Paddle.bottom:
            if self.rightOfBall == Paddle.x or self.leftOfBall == Paddle.x:
                dx = - dx 
                dy = - dy
            
      

        

