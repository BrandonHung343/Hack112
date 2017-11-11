import pygame
import pygameFramework

class bouncingBall(pygameFramework.PygameGame):
    def init(self):
        super(bouncingBall, self).__init__()
        self.color = (0,255,0)
        self.cx = 100
        self.cy = 100
        self.r = 5
        self.dy = 5
        self.currDy = 0
        self.upHeight = 10
        self.jump = False
        self.ball = ((self.cx, self.cy), self.r, self.color)
        self.image = pygame.Surface((2*self.r, 2*self.r), pygame.SRCALPHA)
        
    def getBall(self):
        self.ball = ((self.cx, self.cy), self.r, self.color)
    
    def drawBall(self, screen):
        pygame.draw.circle(screen, self.color, (self.cx, self.cy), self.r)
    
    def keyPressed(self, keyCode, modifier):
        if not self.jump: self.jump = True
    
    def redrawAll(self, screen):
        self.drawBall(screen)
    
    def timerFired(self, dt):
        if self.currDy >= self.upHeight:
            self.currDy = 0
            self.jump = False
        
        if self.jump:
            self.cy -= self.dy
            self.currDy += 1/2
        else:
            self.cy += self.dy
    
game = bouncingBall()
game.run()

