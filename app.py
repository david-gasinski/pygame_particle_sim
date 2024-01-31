
import pygame
import sys
from settings import *
from body import Body
import numpy as np

class App:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(DIMENSIONS)
        self.running = True
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.body = Body(np.asarray([[200,200, 100]]), 10000, (0,0,255), 10, BodyType.PARTICLE)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
            
            dt = self.clock.tick() / 10000

            self.screen.fill((255,255,255))

            self.body.update()
            self.body.render(self.screen)    
        
            pygame.display.update()

if __name__ == '__main__':
    app = App()
    app.run()