# GENERATE THE WORLD & ITS ROBOTS

# use pyrosim to generate a link
import pyrosim.pyrosim as pyrosim

# variables
[length, width, height] = [1, 1, 1]
[x, y, z] = [0, 0, 0.5]


def Create_World():
    # store info about world in world.sdf
    pyrosim.Start_SDF("world.sdf")
    # individual cube
    pyrosim.Send_Cube(name="box", pos=[x, y, z], size=[length, width, height])
    # read it in and simulate it in simulate.py and close file
    pyrosim.End()


Create_World()


def Create_Robot():
    # store info about the robot
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="torso", pos=[x, y, z], size=[length, width, height])
    pyrosim.End()


Create_Robot()

# NOTE: you must run this to generate the box.sdf file so it can be pulled into the simulation
