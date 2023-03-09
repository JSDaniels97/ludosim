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
    pyrosim.Send_Cube(name="Link0", pos=[0, 0, 0.5],
                      size=[1, 1, 1])
    # joint0_1
    # Joints with no upstream joint have absolute positions.
    # Every other joint has a position relative to its upstream joint.
    pyrosim.Send_Joint(name="Link0_Link1", parent="Link0",
                       child="Link1", type="revolute",
                       position=[0, 0, 1])
    # link 1
    pyrosim.Send_Cube(name="Link1", pos=[0, 0, 0.5],
                      size=[1, 1, 1])
    # joint1_2
    pyrosim.Send_Joint(name="Link1_Link2", parent="Link1",
                       child="Link2", type="revolute",
                       position=[0, 0, 1])
    # link 2
    pyrosim.Send_Cube(name="Link2", pos=[0, 0, 0.5],
                      size=[1, 1, 1])
    # joint2_3
    pyrosim.Send_Joint(name="Link2_Link3", parent="Link2",
                       child="Link3", type="revolute",
                       position=[0, 0.5, 0.5])
    # link 3
    pyrosim.Send_Cube(name="Link3", pos=[0, 0.5, 0],
                      size=[1, 1, 1])
    # joint3_4
    pyrosim.Send_Joint(name="Link3_Link4", parent="Link3",
                       child="Link4", type="revolute",
                       position=[0, 1, 0])
    # link 4
    pyrosim.Send_Cube(name="Link4", pos=[0, 0.5, 0],
                      size=[1, 1, 1])
    # joint4_5
    pyrosim.Send_Joint(name="Link4_Link5", parent="Link4",
                       child="Link5", type="revolute",
                       position=[0, 0.5, 0])
    # link 5
    pyrosim.Send_Cube(name="Link5", pos=[0, 0, -1],
                      size=[1, 1, 1])
    # joint5_6
    pyrosim.Send_Joint(name="Link5_Link6", parent="Link5",
                       child="Link6", type="revolute",
                       position=[0, 0, -0.5])
    # link 6
    pyrosim.Send_Cube(name="Link6", pos=[0, 0, -1.5],
                      size=[1, 1, 1])

    # end pyrosim
    pyrosim.End()


Create_Robot()


def robot_prac():
    # store info about the robot
    pyrosim.Start_URDF("robot_prac.urdf")

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


robot_prac()

# NOTE: you must run this to generate the box.sdf file so it can be pulled into the simulation
