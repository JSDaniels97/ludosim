# use pyrosim to generate a link
import pyrosim.pyrosim as pyrosim

# store info about world in world.sdf
pyrosim.Start_SDF("box.sdf")
pyrosim.Send_Cube(name="box", pos=[0, 0, 0.5], size=[1, 1, 1])

# read it in and simulate it in simulate.py and close file
pyrosim.End()
