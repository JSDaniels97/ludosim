import time
import pybullet as p

# connect to physics server
physicsClient = p.connect(p.GUI)

# read in the world into the server
p.loadSDF("box.sdf")

# do the following within the world
for i in range(1000):
    p.stepSimulation()
    time.sleep(1/60)
    print(i)
p.disconnect()
