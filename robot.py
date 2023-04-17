import pybullet as p  # type: ignore
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK


# CLASS ROBOT
class ROBOT:

    # initialize sensing and saves data
    def __init__(self):

        self.robotId = p.loadURDF("body.urdf")  # floor
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.nn = NEURAL_NETWORK("brain.nndf")
        self.Prepare_to_Act()

    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, i):
        for sensor in self.sensors.values():
            sensor.Get_Value(i)  # modifies sensor.values in place

    def Think(self, i):
        self.nn.Print()

    # initialize motor movement and saves data
    def Prepare_to_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)
        for motor in self.motors.values():
            motor.Prepare_to_Act()

    def Act(self, i):
        for motor in self.motors.values():
            motor.Set_Value(self, i)
