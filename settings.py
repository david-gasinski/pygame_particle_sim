from enum import Enum

# APP SETTINGS
WIDTH = 800
HEIGHT = 800
DIMENSIONS = [WIDTH, HEIGHT]
TITLE = "Particle Simulator"

# PHYSICS
STARTING_PARTICLES = 20
GRAVITY = 9.81 
UPDATE_RATE = 0.005
DRAG_COEFFICIENT = 0.47 # static for simulation purposes
LIQUID_DENSITY = 1.204  # density of air at 101kPa and 273K  

# COLLISION BODIES
class BodyType(Enum):
    PARTICLE = 1
    BORDER = 2
    MEDIUM = 3 # liquid or gas

    @classmethod
    def get_body_from_id(cls, id):
        return cls(id)