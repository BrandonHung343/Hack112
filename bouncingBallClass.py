import pygame

class bouncingBall(object):
    def __init__(self):
        sWidth, sHeight = 300, 500
        self.color = (0,255,0)
        self.cx = sWidth/2
        self.cy = 100
        self.width = sWidth
        self.height = sHeight
        self.r = 5
        self.dy = 5
        self.currDy = 0
        self.upHeight = 10
        self.screenMargin = 100
        self.scrollY =0
        self.jump = False
        self.ball = ((self.cx, self.cy), self.r, self.color)
        self.image = pygame.Surface((2*self.r, 2*self.r), pygame.SRCALPHA)
        
    def getY(self):
        return self.cy
    
    def getBall(self):
        self.ball = ((self.cx, self.cy), self.r, self.color)
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, 
                            (int(self.cx), self.cy-self.scrollY), self.r)
    
    def key(self):
        if not self.jump: self.jump = True
            
    def update(self, scroll):
        self.scrollY = scroll
        if self.cy <= self.scrollY + self.screenMargin + self.upHeight:
            self.scrollY = self.cy - self.screenMargin
            
        if self.currDy >= self.upHeight:
            self.currDy = 0
            self.jump = False
        
        if self.jump:
            if self.cy + self.upHeight > self.screenMargin:
                self.cy -= self.dy
            self.currDy += 1/2
        else:
            self.cy += self.dy
