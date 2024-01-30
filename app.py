
import pygame
import sys
from settings import *


class App:
    def __init__(self):
        pygame.init()
        self.running = True
        self.screen = pygame.display.set_mode(DIMENSIONS)
        pygame.display.set_caption(TITLE)
        self.clock = pygame.Time.Clock()

    def run(self):
        while self.running:
            for evene in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
            
            dt = self.clock.tick() / 10000
            self.screen.fill()
            pygame.display.update()

if __name__ == '__app__':
    app = App()
    app.run()