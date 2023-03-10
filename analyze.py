# add libraries
import matplotlib.pyplot as plt
import numpy
import matplotlib.pyplot

# load file
backLegSensorValues = numpy.load('data/sensordata.npy')
print(backLegSensorValues)

# plot
plt.plot(backLegSensorValues)
matplotlib.pyplot.show()
