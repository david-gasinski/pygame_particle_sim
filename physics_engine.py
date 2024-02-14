from body import Body
import numpy as np
import math
from settings import GRAVITY, UPDATE_RATE, DRAG_COEFFICIENT, LIQUID_DENSITY
 
def _magintude(arr):
    return np.linalg.norm(arr)

def _unit_vector(arr):
    return arr / _magintude(arr)

class PhysicsEngine():
    def __init__(self):
        self.body_list = []
    
    def drag(self, target: Body):
        drag = 0.5 * DRAG_COEFFICIENT * LIQUID_DENSITY * (target.surface_area / 2) * math.pow(target.velocity[0][1], 2)
        target.update_force(np.asarray([[0, -drag, 0]]))

    def motion(self, target: Body):
        target.update_velocity(target.velocity + (target.force / target.mass))
        target.pos = target.pos + (target.velocity * UPDATE_RATE)
    
    def gravity(self, target: Body):
        target.velocity[0][1] += (GRAVITY * UPDATE_RATE)

    def run(self, iterations):
        for body in self.body_list:
            # apply motions
            print(body.velocity)

            self.gravity(body)
            self.drag(body)
            self.motion(body)
            
