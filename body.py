import pygame
import numpy as np
from settings import UPDATE_RATE, BodyType, GRAVITY, DRAG_COEFFICIENT, LIQUID_DENSITY
import math


class Body:
    def __init__(self, vector_arr: list, mass: float, color: pygame.Color, radius: int, body_type: BodyType):
        self.color = color
        self.body_type = body_type
        self.pos = vector_arr
        self.velocity = np.array([[0,0,0]])
        self.force = np.array([[0,0,0]])

        self.radius = radius
        self.surface_area = 4 * math.pi * math.pow(self.radius, 2)
        self.mass = mass
        

    def render(self, surface):
        pygame.draw.circle(surface, self.color, (self.pos[0][0], self.pos[0][1]), self.radius)

    # change speed and direction
    def update_velocity(self, new_vel):
        self.velocity = self.velocity + new_vel
    
    # apply a force
    def update_force(self, new_force):
        self.force = new_force

    # update vel and pos
    def update(self):
        # calulate and apply drag in air
        drag = 0.5 * DRAG_COEFFICIENT * LIQUID_DENSITY * self.surface_area / 2 * math.pow(self.velocity[0][1], 2)
        self.update_force(np.asarray([[0, -drag, 0]]))

        # v = u + (force/mass)*t
        self.velocity = self.velocity + (self.force / self.mass) * UPDATE_RATE # change to delta time
        
        # update y if terminal hasn't been reached
        self.velocity[0][1] += (GRAVITY * UPDATE_RATE)

        # d = s * t
        self.pos = self.pos + (self.velocity * UPDATE_RATE) 

    def collisions(self):
        # iterate through list of collision bodies and check if bounds intersect
        
        # if barrier is hit, reverse direction
        return