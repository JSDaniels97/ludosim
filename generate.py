# GENERATE THE WORLD

# use pyrosim to generate a link
import pyrosim.pyrosim as pyrosim

# # store info about world in world.sdf
pyrosim.Start_SDF("boxes.sdf")
[length, width, height] = [1, 1, 1]
[x, y, z] = [0, 0, 0.5]

pyrosim.Send_Cube(name="box", pos=[x, y, z], size=[length, width, height])
pyrosim.Send_Cube(name="box2", pos=[1, y, 1.5], size=[length, width, height])

# read it in and simulate it in simulate.py and close file
pyrosim.End()

# NOTE: you must run this to generate the box.sdf file so it can be pulled into the simulation
