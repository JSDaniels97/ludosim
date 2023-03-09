# SIMULATE THE WORLD (TEST)

# import libraries
import time
import pybullet as p
import pybullet_data

# connect to physics server
physicsClient = p.connect(p.GUI)
# connect to additional data for server
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# add the forces (i.e., gravity)
p.setGravity(0, 0, -9.8)

# add a floor
planeId = p.loadURDF("plane.urdf")

# read in the world into the server
p.loadSDF("box.sdf")

# do the following within the world
for i in range(1000):
    p.stepSimulation()
    time.sleep(1/60)
    print(i)
p.disconnect()
