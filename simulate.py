# SIMULATE THE WORLD

# import libraries
import time
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy

# connect to physics server
physicsClient = p.connect(p.GUI)
# connect to additional data for server
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# add the forces (i.e., gravity)
p.setGravity(0, 0, -9.8)

# add urdfs (Unified Robot Description Format)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")

# read in the world into the server
p.loadSDF("world.sdf")

# prepare to read in robots
pyrosim.Prepare_To_Simulate(robotId)

# empty array for storing sensor values
backLegSensorValues = numpy.zeros(100)
frontLegSensorValues = numpy.zeros(100)
# exit()

# do the following within the world
for i in range(100):
    p.stepSimulation()

    # store sensor values during each step
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("backleg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("frontleg")
    # print(backLegTouch)

    time.sleep(1 / 60)
    # print(i)

# # print sensor values
# print(backLegSensorValues)

# save sensor values to file
numpy.save('data/backLegSensorValues', backLegSensorValues)
numpy.save('data/frontLegSensorValues', frontLegSensorValues)

p.disconnect()
