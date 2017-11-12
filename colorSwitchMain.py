import pygame
import pygameFramework
import bouncingBallClass

class colorSwitch(pygameFramework.PygameGame):
    def init(self):
        self.scrollY = 0
        self.ball = bouncingBallClass.bouncingBall()
    def mousePressed(self, x, y): pass
    def keyPressed(self, keyCode, modifier):
        self.ball.key()
    def timerFired(self, dt):
        self.ball.update(self.scrollY)
    def redrawAll(self, screen):
        self.ball.draw(screen)

game = colorSwitch()
game.run()