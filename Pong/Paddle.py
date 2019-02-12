import pygame
import grove


class Paddle(object):
    def __init__(paddle, screensize, xPos):

        # im not sure what this does tbh , but it doesnt work without it :)
        paddle.screensize = screensize

        # starting x for paddle
        paddle.centerx = int (xPos)
        # starting y
        paddle.centery = int (screensize[1]*0.5)
        #paddle attributes        
        paddle.height = 100;
        paddle.width = 10;

        paddle.rect = pygame.Rect(0, paddle.centery-int(paddle.height*0.5),
                                 paddle.width, paddle.height)

        # paddle white by default
        paddle.color = (200,200,200)
        paddle.speed = 3
        # if no input , paddle does not move
        paddle.direction = 0

    def update (paddle):

        paddle.centery += paddle.direction*paddle.speed
        # paddle collision
        paddle.rect.center = (paddle.centerx, paddle.centery)

        #stops paddle exiting top and bottom of screen
        if paddle.rect.top < 0:
            paddle.rect.top = 0
        if paddle.rect.bottom > paddle.screensize[1]-1:
            paddle.rect.bottom = paddle.screensize[1] -1


    def render (paddle, screen):
        pygame.draw.rect(screen, paddle.color, paddle.rect, 0)
        # black outline around paddle , probs wont need this when displayed on LED screen
        pygame.draw.rect(screen, (0,0,0), paddle.rect, 1)
    


