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
    pyrosim.Send_Cube(name="Link0", pos=[0, 0, 0.5],
                      size=[1, 1, 1])
    # connecting joint
    # Joints with no upstream joint have absolute positions.
    # Every other joint has a position relative to its upstream joint.
    pyrosim.Send_Joint(name="Link0_Link1", parent="Link0",
                       child="Link1", type="revolute",
                       position=[0, 0, 1])
    # leg
    pyrosim.Send_Cube(name="Link1", pos=[0, 0, 0.5],
                      size=[1, 1, 1])
    pyrosim.End()


Create_Robot()

# NOTE: you must run this to generate the box.sdf file so it can be pulled into the simulation
