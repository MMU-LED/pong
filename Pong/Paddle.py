import keyboard
import GenericObject
import pygame


class Paddle(GenericObject):
    """description of class"""

    x #variables
    y
    paddleHeight = 5*scale #j
    top = y - paddleHeight
    bottom = y + paddleHeight
    #dx = 5*scale
    s #speed :) 
    dy = s*scale

    def __init__ (self, x, y, s): #initiate class (constructor?)
        self.x = x
        self.y = y 
        self.s = s

    def render(): #this needs doing

    def move(): #move up & down 
        if keyboard.is_pressed('up'):
            print('You Pressed A Key!')
            y = y + dy;
        if keyboard.is_pressed('down'):
            print('You Pressed A Key!')
            y = y - dy;

    def edgeDetect(): #stop user taking paddle of top of screen
        if y - paddleheight >height:
            y  = height
        if y<0:
            y = 0

    def unfreeze(): #unfreeze method inherited from GenericObject
        dy = 5*scale

   # def bounce(self, Ball): #might be unecessary, needs testing
        
        
         

 