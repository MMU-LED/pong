import pygame
import random
import decimal
#pygame.org.docs
class Ball(object):
    def __init__(ball, screensize,scale):
        ball.scale = scale 
        ball.screensize = screensize
        #pygame does not work with decimal apparently so needs to be INT
        ball.centerx = int(screensize[0]*0.5)                    
        ball.centery = int(screensize[1]*0.5)
        #size of ball
        ball.raduis = scale*6

        #collision detection around ball                                                         
        ball.rect = pygame.Rect(ball.centerx-ball.raduis,        #top left
                                ball.centery-ball.raduis,        #starting point
                                ball.raduis, ball.raduis)    #size
        # green ball 
        ball.color = (100,255,100)   
        # x / y movement the same currently at 1 - 1
        if (random.randint(1, 2) ==1):
           ball.direction = [-1,random.randint(50, 100)/100]
        else:
            ball.direction = [-1,random.randint(-100, -50)/100]
        # speed of ball
        ball.speed = 0.33*scale
     
        ball.hit_edge_left = False
        ball.hit_edge_right = False

    def update(ball, player_paddle, player2_paddle, scale):

        #movement for ball x + y
        ball.centerx += ball.direction[0] * ball.speed
        ball.centery += ball.direction[1] * ball.speed
        # moving collision box around ball
        ball.rect.center = (ball.centerx, ball.centery)          

        #if ball hits top of screen, bounce down
        if ball.rect.top <= 11*scale:                                   
            ball.direction[1] = ball.direction[1]*-1
        #if ball hits bottom of screen, bounce up
        elif ball.rect.bottom >= ball.screensize[1]-1:           
            ball.direction[1] = ball.direction[1]*-1

        #If ball hits right of screen , p1( left ) wins
        if ball.rect.right >= ball.screensize[0]-1:
            ball.hit_edge_right = True  
        #If ball hits left of screen , p2( right ) wins
        elif ball.rect.left<=0:
            ball.hit_edge_left = True

        if ball.rect.colliderect(player_paddle.rect):
            ball.direction[0] = -1
            #ball.speed += 0.4
            ball.speed += (scale*0.1)
        
        if ball.rect.colliderect(player2_paddle.rect):
            ball.direction[0] = 1
            #ball.speed += 0.4
            ball.speed += (scale*0.03)
            
    def render(ball, screen, scale):
        pygame.draw.circle(screen, ball.color, ball.rect.center, scale*2, 0)
        # black outline around ball , probs wont need this when displayed on LED screen - commented it out just in case we still need it
        # pygame.draw.circle(screen, (0,0,0), ball.rect.center, ball.raduis, 1)


        

