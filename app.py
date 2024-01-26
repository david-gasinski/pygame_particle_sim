
import random
import pygame
from obj_handler import ObjHandler
from obj.particle import Particle

# init pygame
pygame.init()

WIDTH = 800
HEIGHT = 800
GRAVITY = 1
DIMENSIONS = [WIDTH, HEIGHT]

# set up windows
screen = pygame.display.set_mode(DIMENSIONS)
obj_handler = ObjHandler()
# render 20 new particles
# random pos
for i in range(0, 20):
    obj_handler.add_object(Particle(random.randint(0,WIDTH), random.randint(0,HEIGHT), screen))

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255,255,255))
    
    for obj in obj_handler.get_objects():
        obj.tick()
        obj.render()
    
    
    # set up background

    pygame.display.flip()

pygame.quit()