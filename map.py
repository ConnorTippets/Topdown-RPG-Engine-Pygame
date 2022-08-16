from properties import *
from pygame import Rect
import os, sys

levels = {}
def generate_levels():
    #(this took forever holy fuck)
    #Import the levels from the levels folder into a dictionary of modules
    #That can be used to get maps from
    d = os.getcwd()+'/levels'
    ls = os.listdir(d)
    for l in ls:
        if not l.startswith('level'):
            continue
        #Two magic lines of code that I do not feel qualified to explain lmfao
        _temp = __import__('levels', globals(), locals(), [l])
        levels[l] = eval(f'_temp.{l.replace(".py", "")}', globals(), locals())

generate_levels()
class Map:
    def __init__(self, levelx=0, levely=0):
        self.level = (levelx, levely)
        self.levelx, self.levely = self.level
        self.map = []
        self.update_map()
    
    def update_map(self):
        #Update the map with the current map using the levels dictionary
        self.levelx, self.levely = self.level
        try:
            _ = levels[f'levelx{self.levelx}y{self.levely}.py']
        except:
            _ = type('_', (), {'map': [0]*(mCols*mRows)})
            self.level = [sys.maxsize]*2
            self.levelx, self.levely = self.level
        self.map = _.map
        self.update_collision()
    
    def update_collision(self):
        #Create a list of rectangles that can
        #Be used to check for collisions and
        #Draw the map (used in main.py)
        self.collision = []
        for y in range(mRows):
            for x in range(mCols):
                xy = self.map[y*mRows+x]
                if xy > 0:
                    r = Rect(x*tSize+1,y*tSize+1, tSize-1,tSize-1)
                else:
                    r = Rect(20000,20000, 1,1)
                self.collision.append(r)
    
    def collide(self, rect):
        #Checks if the level collides with a rectangle
        #If it does, return True
        #If it doesn't, return False
        if not rect.collidelist(self.collision) == -1:
            return True
        return False
    
    def scroll(self, x, y):
        #Scroll the map based on an x and y
        mMaxX = tSize*mCols
        mMaxY = tSize*mRows
        if x < 0:
            #If the x is less than 0, set it to the max
            self.level = (self.levelx-1, self.levely)
            self.update_map()
            x = mMaxX-1
        elif x > mMaxX:
            #If the x is more than the max, set it to 0
            self.level = (self.levelx+1, self.levely)
            self.update_map()
            x = 1
        if y < 0:
            #If the y is less than 0, set it to the max
            self.level = (self.levelx, self.levely+1)
            self.update_map()
            y = mMaxY-1
        elif y > mMaxY:
            #If the y is more than the max, set it to 0
            self.level = (self.levelx, self.levely-1)
            self.update_map()
            y = 1
        return (x, y)
    
map = Map()
