import numpy as np
 
def _magintude(arr):
    return np.linalg.norm(arr)

def _unit_vector(arr):
    return arr / _magintude(arr)

class PhysicsEngine():
    def __init__(self):
        pass