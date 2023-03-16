# SIMULATE THE WORLD

# import libraries
import time

import numpy as np
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import random

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
backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)
# exit()

# open-loop movement
# targetAngles = numpy.sin(numpy.linspace(0, 2*numpy.pi, 1000))
targetAngles = numpy.sin(numpy.linspace(-numpy.pi/4, numpy.pi/4, 1000))
# print(targetAngles)
numpy.save('data/targetAngles', targetAngles)

exit()

# do the following within the world
for i in range(1000):  # number of steps
    p.stepSimulation()

    # store sensor values during each step
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("backleg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("frontleg")
    # print(backLegTouch)

    # simulate motors
    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotId,  # identify the robot the motor should attach to
        jointName=b'torso_backleg',  # what joint should the motor attach to, i.e., rotational force
        controlMode=p.POSITION_CONTROL,  # motor control, positional or velocity
        targetPosition=random.randrange(int(-3.1415/2.0), int(3.1415/2.0)),  # target position, i.e., angle between two links
        maxForce=50  # max force applied in Newton-metres
    )
    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotId,  # identify the robot the motor should attach to
        jointName=b'torso_frontleg',  # what joint should the motor attach to, i.e., rotational force
        controlMode=p.POSITION_CONTROL,  # motor control, positional or velocity
        targetPosition=random.randrange(int(-3.1415/2.0), int(3.1415/2.0)),  # target position, i.e., angle between two links
        maxForce=50  # max force applied in Newton-metres
    )
    time.sleep(1 / 60)
    # print(i)

# # print sensor values
# print(backLegSensorValues)

# save sensor values to file
numpy.save('data/backLegSensorValues', backLegSensorValues)
numpy.save('data/frontLegSensorValues', frontLegSensorValues)

p.disconnect()
