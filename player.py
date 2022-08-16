from properties import *
from pygame import Rect
class Player:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
    
    def handle_controls_x(self, joystick_x, run=False):
        #Move the player based on a -1 to 1 value
        #If its -1, move the player left 10 pixels (20 if running)
        #If its 1, move the player right 10 pixels (20 if running)
        self.x+=(joystick_x*(20 if run else 10))
    
    def handle_controls_y(self, joystick_y, run=False):
        #Move the player based on a -1 to 1 value
        #If its -1, move the player down 10 pixels (20 if running)
        #If its 1, move the player up 10 pixels (20 if running)
        self.y+=-(joystick_y*(20 if run else 10))
    
    def update_rectangle(self):
        r = Rect(int(self.x-(self.w/2)),int(self.y-(player.y/2)), self.w,self.h)
        r.center = [self.x, self.y]
        return r

#Initialize the player in the middle of the screen (variables are defined in properties.py)
player = Player(int(wWidth/2), int(wHeight/2), pWidth, pHeight)
