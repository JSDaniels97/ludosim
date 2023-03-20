import pybullet as p  # type: ignore


# CLASS WORLD
class WORLD:

    # load in the floor
    def __init__(self):
        self.planeId = p.loadURDF("plane.urdf")  # floor
        p.loadSDF("world.sdf")
