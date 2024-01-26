import pygame
class Particle:
    def __init__(self, x: int, y: int, surface: pygame.Surface) -> None:
        self.x = x
        self.y = y
        self.surface = surface

    def render(self):
        pygame.draw.circle(self.surface,(0,0,255), (self.x, self.y), 10)

    def tick(self):
        if (self.y < 800):
            self.gravity = 0.5
            self.y += self.gravity
        else:
            self.gravity = -4
        
