
import pygame
import sys
from settings import *
from body import Body
import numpy as np
from physics_engine import PhysicsEngine

class App:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(DIMENSIONS)
        self.running = True
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.physics = PhysicsEngine()
        self.physics.body_list.append(Body([[200,200,200]], 100, (0,0,255), 5, BodyType.PARTICLE))
    
    def run(self):
        iterations = 0
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
            
            dt = self.clock.tick() / 10000

            self.screen.fill((255,255,255))


            self.physics.run(iterations) 

            for target in self.physics.body_list:
                target.render(self.screen)
        
            iterations += 1
            pygame.display.update()

if __name__ == '__main__':
    app = App()
    app.run()