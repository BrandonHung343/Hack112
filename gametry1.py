import pygame
from pygameGame import *
import math, string, copy, time, random
    
class gameObject(pygame.sprite.Sprite):
    def __init__(self,x,y,r,angle,screen):
        self.x = x
        self.y = y
        self.r = r
        self.rect = ()
        self.angle = angle
        self.screen = screen
        self.color = (0,0,0)
        self.mask = pygame.mask.from_surface(screen)
    
    def draw(self):
        x = self.x
        y = self.y
        r = self.r
        self.rect = (x-r, y-r, 2*r, 2*r)

class CirclePurple(gameObject):
    def draw(self):
        super().draw()
        self.color = (153,153,255)
        pygame.draw.arc(self.screen, self.color , self.rect, 
                        self.angle + 3*math.pi/4, 
                        self.angle + 5*math.pi/4,10)
                        
class CirclePink(gameObject):
    def draw(self):
        super().draw()
        self.color = (255,153,204)
        pygame.draw.arc(self.screen, self.color, self.rect, 
                        self.angle + math.pi/4,
                        self.angle + 3*math.pi/4,10)
                        
class CircleYellow(gameObject):
    def draw(self):
        super().draw()
        self.color = (255,255,153)
        pygame.draw.arc(self.screen, self.color, self.rect,
                        self.angle + -math.pi/4,
                        self.angle + math.pi/4, 10)
                        
class CircleGreen(gameObject):
    def draw(self):
        super().draw()
        self.color = (153,255,204)
        pygame.draw.arc(self.screen, self.color, self.rect, 
                        self.angle + -3*math.pi/4,
                        self.angle + -math.pi/4,10)
                        
class Cursor(gameObject):
    def __init__(self, screenWidth, screenHeight):
        self.x = screenWidth//2
        self.y = screenHeight - 20
        self.r = 10
        self.cursorSpeed = 5
        self.color = (255,255,153) #yellow
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x,self.y), self.r)
        
    def update(self, keysDown):
        if keysDown(pygame.K_LEFT):
            self.x -= self.cursorSpeed

        if keysDown(pygame.K_RIGHT):
            self.x += self.cursorSpeed
            
        if keysDown(pygame.K_UP):
            self.y -= self.cursorSpeed
        
        if keysDown(pygame.K_DOWN):
            self.y += self.cursorSpeed

"""
class myProject(PygameGame):
    def init(self):
        
        self.purple = (153,153,255)
        self.pink = (255,153,204)
        self.yellow = (255,255,153)
        self.green = (153,255,204)
        
        #circle
        self.circleList = []
        self.angleList = []
        
        self.cursor = Cursor(self.width, self.height)
        
        #layers
        self.screenPurple = pygame.display.set_mode((self.width, self.height))
        self.screenPink = pygame.display.set_mode((self.width, self.height))
        self.screenYellow = pygame.display.set_mode((self.width, self.height))
        self.screenGreen = pygame.display.set_mode((self.width, self.height))
        
        #groups
        self.purpleGrp = pygame.sprite.Group()
        self.pinkGrp = pygame.sprite.Group()
        self.yellowGrp = pygame.sprite.Group()        
        self.greenGrp = pygame.sprite.Group()
        
    def mousePressed(self, x, y):
        r = random.randint(40,50)
        self.circleList.append((x,y,r))
        self.angleList.append(0)
    
    def timerFired(self, dt):
        for i in range (len(self.angleList)):
            self.angleList[i] += 0.05
            
        self.cursor.update(self.isKeyPressed)
        
        # if self.cursor.color == self.purple:
        #     for pinkArc in self.pinkGrp:
        #         if pygame.sprite.collide_mask(self.cursor, pinkArc) != None:
        #             print ("COLLIDED WITH PINK")
        #     for yellowArc in self.yellowGrp:
        #         if pygame.sprite.collide_mask(self.cursor, yellowArc) != None:
        #             print ("COLLIDED WITH YELLOW")
        #     for greenArc in self.greenGrp:
        #         if pygame.sprite.collide_mask(self.cursor, greenArc) != None:
        #             print ("COLLIDED WITH GREEN")
        # 
        # elif self.cursor.color == self.pink:
        #     for purpleArc in self.purpleGrp:
        #         if pygame.sprite.collide_mask(self.cursor, purpleArc) != None:
        #             print ("COLLIDED WITH PURPLE")
        #     for yellowArc in self.yellowGrp:
        #         if pygame.sprite.collide_mask(self.cursor, yellowArc) != None:
        #             print ("COLLIDED WITH YELLOW")
        #     for greenArc in self.greenGrp:
        #         if pygame.sprite.collide_mask(self.cursor, greenArc) != None:
        #             print ("COLLIDED WITH GREEN")
        # 
        # elif self.cursor.color == self.yellow:
        #     for purpleArc in self.purpleGrp:
        #         if pygame.sprite.collide_mask(self.cursor, purpleArc) != None:
        #             print ("COLLIDED WITH PURPLE")
        #     for pinkArc in self.pinkGrp:
        #         if pygame.sprite.collide_mask(self.cursor, pinkArc) != None:
        #             print ("COLLIDED WITH PINK")
        #     for greenArc in self.greenGrp:
        #         if pygame.sprite.collide_mask(self.cursor, greenArc) != None:
        #             print ("COLLIDED WITH GREEN")
        #             
        # elif self.cursor.color == self.green:
        #     for purpleArc in self.purpleGrp:
        #         if pygame.sprite.collide_mask(self.cursor, purpleArc) != None:
        #             print ("COLLIDED WITH PURPLE")
        #     for yellowArc in self.yellowGrp:
        #         if pygame.sprite.collide_mask(self.cursor, yellowArc) != None:
        #             print ("COLLIDED WITH YELLOW")
        #     for pinkArc in self.pinkGrp:
        #         if pygame.sprite.collide_mask(self.cursor, pinkArc) != None:
        #             print ("COLLIDED WITH PINK")
        
    def redrawAll(self, screen):
        for i in range (len(self.circleList)):
            x, y, r = self.circleList[i]
            angle = self.angleList[i]
            
            circlePurple = CirclePurple(x,y,r, angle, self.screenPurple)
            circlePink = CirclePink(x,y,r, angle, self.screenPink)
            circleYellow = CircleYellow(x,y,r, angle, self.screenYellow)
            circleGreen = CircleGreen(x,y,r, angle, self.screenGreen)
            
            self.purpleGrp.add(circlePurple)
            self.pinkGrp.add(circlePink)
            self.yellowGrp.add(circleYellow)
            self.greenGrp.add(circleGreen)
            
            circlePurple.draw()
            circlePink.draw()
            circleYellow.draw()
            circleGreen.draw()
            
            screen.blit(self.screenPurple, (0,0))
            screen.blit(self.screenPink, (0,0))
            screen.blit(self.screenYellow,(0,0))
            screen.blit(self.screenGreen, (0,0))
        
        self.cursor.draw(screen) """

class myProject(PygameGame):
    def init(self):
        
        self.purple = (153,153,255)
        
        #circle
        self.circleList = []
        self.angleList = []
        
        self.cursor = Cursor(self.width, self.height)
        
        #layers
        self.screenPurple = pygame.display.set_mode((self.width, self.height))
        
        #groups
        self.purpleGrp = pygame.sprite.Group()
        
    def mousePressed(self, x, y):
        r = random.randint(40,50)
        self.circleList.append((x,y,r))
        self.angleList.append(0)
    
    def timerFired(self, dt):
        for i in range (len(self.angleList)):
            self.angleList[i] += 0.05
            
        self.cursor.update(self.isKeyPressed)
        
    def redrawAll(self, screen):
        for i in range (len(self.circleList)):
            x, y, r = self.circleList[i]
            angle = self.angleList[i]
            
            circlePurple = CirclePurple(x,y,r, angle, self.screenPurple)
            
            self.purpleGrp.add(circlePurple)
            
            circlePurple.draw()
            
            screen.blit(self.screenPurple, (0,0))
        
        self.cursor.draw(screen)
    
#creating and running the game
game = myProject()
game.run()