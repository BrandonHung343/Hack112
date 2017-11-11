import pygame
from pygamegame import PygameGame

class myProject(pygamegame):
    def init(self):
        self.message = "World Helo"
    def mousepressed(self, x, y):
        print(self.message)

#creating and running the game
game = myProject()
game.run()