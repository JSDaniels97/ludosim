# SIMULATE THE WORLD

# import libraries
import time
import pybullet as p

# connect to physics server
physicsClient = p.connect(p.GUI)

# add the forces (i.e., gravity)
p.setGravity(0, 0, -9.8)

# read in the world into the server
p.loadSDF("box.sdf")

# do the following within the world
for i in range(1000):
    p.stepSimulation()
    time.sleep(1/60)
    print(i)
p.disconnect()
