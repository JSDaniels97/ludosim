# GENERATE THE WORLD & ITS ROBOTS

# use pyrosim to generate a link
import pyrosim.pyrosim as pyrosim


def Create_World():
    # store info about world in world.sdf
    pyrosim.Start_SDF("world.sdf")
    # individual cube
    pyrosim.Send_Cube(name="box", pos=[5, 5, 0.5],
                      size=[1, 1, 1])
    # read it in and simulate it in simulate.py and close file
    pyrosim.End()


Create_World()


def Create_Robot():
    # store info about the robot
    pyrosim.Start_URDF("body.urdf")
    # torso
    pyrosim.Send_Cube(name="torso", pos=[0, 0, 0.5],
                      size=[1, 1, 1])
    # connecting joint
    pyrosim.Send_Joint(name="torso_leg", parent="torso",
                       child="leg", type="revolute",
                       position=[0.5, 0, 1])
    # leg
    pyrosim.Send_Cube(name="leg", pos=[1, 1, 1.5],
                      size=[1, 1, 1])
    pyrosim.End()


Create_Robot()

# NOTE: you must run this to generate the box.sdf file so it can be pulled into the simulation
