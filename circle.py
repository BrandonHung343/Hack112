import pygame
from pygameGame import *
import math, string, copy, time, random
import numpy as np


def remove_holes(surface, background=(0, 0, 0)):
    """
    Removes holes caused by aliasing.

    The function locates pixels of color 'background' that are surrounded by pixels of different colors and set them to
    the average of their neighbours. Won't fix pixels with 2 or less adjacent pixels.

    Args:
        surface (pygame.Surface): the pygame.Surface to anti-aliasing.
        background (3 element list or tuple): the color of the holes.

    Returns:
        anti-aliased pygame.Surface.
    """
    
    width, height = surface.get_size()
    array = pygame.surfarray.array3d(surface)
    contains_background = (array == background).all(axis=2)

    neighbours = (0, 1), (0, -1), (1, 0), (-1, 0)

    for row in range(1, height-1):
        for col in range(1, width-1):
            if contains_background[row, col]:
                average = np.zeros(shape=(1, 3), dtype=np.uint16)
                elements = 0
                for y, x in neighbours:
                    if not contains_background[row+y, col+x]:
                        elements += 1
                        average += array[row+y, col+x]
                if elements > 2:  # Only apply average if more than 2 neighbours is not of background color.
                    array[row, col] = average // elements

    return pygame.surfarray.make_surface(array)
    
class gameObject(pygame.sprite.Sprite):
    pass
    
class myProject(PygameGame):
    def init(self):
        
        #circle
        self.circleList = []
        self.angleList = []
    
    def mousePressed(self, x, y):
        self.createCircle(x,y,random.randint(20,50))
        
    def drawCircle(self, x, y, r, angle, screen):
        rect = (x-r, y-r, 2*r, 2*r)
        pygame.draw.arc(screen, (153,153,255), rect, 
                        angle + 3*math.pi/4, 
                        angle + 5*math.pi/4,10)
        pygame.draw.arc(screen, (255,153,204), rect, 
                        angle + math.pi/4,
                        angle + 3*math.pi/4,10)
        pygame.draw.arc(screen, (255,255,153), rect,
                        angle + -math.pi/4,
                        angle + math.pi/4, 10)
        pygame.draw.arc(screen, (153,255,204), rect, 
                        angle + -3*math.pi/4,
                        angle + -math.pi/4,10)
    
    def timerFired(self, dt):
        for i in range (len(self.angleList)):
            self.angleList[i] += 0.05
    
    def createCircle(self,x,y,r):
        self.circleList.append((x,y,r))
        self.angleList.append(0)
        
    def redrawAll(self, screen):
        for i in range (len(self.circleList)):
            x, y, r = self.circleList[i]
            angle = self.angleList[i]
            self.drawCircle(x,y,r, angle, screen)
    
#creating and running the game
game = myProject()
game.run()