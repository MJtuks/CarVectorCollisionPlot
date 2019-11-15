import matplotlib.pyplot as plt
import numpy as np

vehicle1 = (3, 0.1) #(pi1=initialPosition, v1=calculatedVelocity)
vehicle2 = (0, 0.2) #(pi1=initialPosition, v1=calculatedVelocity)

time = np.arange(0, 40, 1)
vehicle1Position = time*vehicle1[1] + vehicle1[0]
vehicle2Position = time*vehicle2[1] + vehicle2[0]

plt.plot(time, vehicle1Position)
plt.plot(time, vehicle2Position)