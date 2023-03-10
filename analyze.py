# add libraries
import matplotlib.pyplot as plt
import numpy
import matplotlib.pyplot

# load file
backLegSensorValues = numpy.load('data/backLegSensorValues.npy')
frontLegSensorValues = numpy.load('data/frontLegSensorValues.npy')
print(backLegSensorValues)
print(frontLegSensorValues)

# plot
plt.plot(backLegSensorValues, linewidth=10)
plt.plot(frontLegSensorValues, linewidth=3)
matplotlib.pyplot.legend()
matplotlib.pyplot.show()
