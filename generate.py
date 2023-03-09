# GENERATE THE WORLD

# use pyrosim to generate a link
import pyrosim.pyrosim as pyrosim

# # store info about world in world.sdf
pyrosim.Start_SDF("box.sdf")
length = 1
width = 2
height = 3
pyrosim.Send_Cube(name="box", pos=[0, 0, 0.5], size=[length, width, height])

# read it in and simulate it in simulate.py and close file
pyrosim.End()

# NOTE: you must run this to generate the box.sdf file so it can be pulled into the simulation
