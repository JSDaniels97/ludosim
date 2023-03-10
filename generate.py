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

    # DESIGN THE BODY
    # link 0
    pyrosim.Send_Cube(name="torso", pos=[0, 0, 1.5],
                      size=[1, 1, 1])
    # joint0_1
    pyrosim.Send_Joint(name="torso_backleg", parent="torso",
                       child="backleg", type="revolute",
                       position=[0, 0, 1])
    # link 1
    pyrosim.Send_Cube(name="backleg", pos=[0, 1, -0.5],
                      size=[1, 1, 1])
    # joint0_2
    pyrosim.Send_Joint(name="torso_frontleg", parent="torso",
                       child="frontleg", type="revolute",
                       position=[0, 0, 1])
    # link 2
    pyrosim.Send_Cube(name="frontleg", pos=[0, -1, -0.5],
                      size=[1, 1, 1])


    # end pyrosim
    pyrosim.End()


Create_Robot()

# NOTE: you must run this to generate the box.sdf file
# so it can be pulled into the simulation
