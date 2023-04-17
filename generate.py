import pyrosim.pyrosim as pyrosim


# GENERATE files of things in the world
# generates links and joints and sends them a urdf file
# NOW it'll also generate neurons and synapses and send them to a nndf file
# neural network description format file

# ... a world with objects
def Create_World():
    pyrosim.Start_SDF("world.sdf")
    width, length, height = 1, 1, 1  # box dimensions
    pyrosim.Send_Cube(name="Box", pos=[-2, -2, 0.5], size=[width, length, height])
    pyrosim.End()


# ...an empty robot (ie., no motor, sensors, brain, etc.)
def Generate_Body():
    pyrosim.Start_URDF("body.urdf")  # stores description of robot's body
    width, length, height = 1, 1, 1  # link dimensions

    # joint naming convention: Parent_Child
    pyrosim.Send_Cube(name="Torso", pos=[1.5, 0, 1.5], size=[width, length, height])
    pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg",
                       type="revolute", position=[1.0, 0, 1.0])
    pyrosim.Send_Cube(name="BackLeg", pos=[-0.5, 0, -0.5], size=[length, height, width])
    pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg",
                       type="revolute", position=[2.0, 0, 1.0])
    pyrosim.Send_Cube(name="FrontLeg", pos=[0.5, 0, -0.5], size=[length, height, width])

    pyrosim.End()


# ... a brain for the empty robot
def Generate_Brain():
    pyrosim.Start_NeuralNetwork("brain.nndf")  # stores description of robot's brain

    # sensor neuron receives values from sensors in Torso
    pyrosim.Send_Sensor_Neuron(name=0, linkName='Torso')

    pyrosim.End()


Create_World()
Generate_Body()
Generate_Brain()
