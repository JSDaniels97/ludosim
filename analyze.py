# add libraries
import matplotlib.pyplot as plt
import numpy
import matplotlib.pyplot

# load file
# backLegSensorValues = numpy.load('data/backLegSensorValues.npy')
# frontLegSensorValues = numpy.load('data/frontLegSensorValues.npy')
# print(backLegSensorValues)
# print(frontLegSensorValues)
targetAngles = numpy.load('data/targetAngles.npy')
# print(targetAngles)


# plot
# plt.plot(backLegSensorValues, linewidth=10)
# plt.plot(frontLegSensorValues, linewidth=3)
plt.plot(targetAngles, linewidth=3)
# matplotlib.pyplot.legend()
matplotlib.pyplot.show()
