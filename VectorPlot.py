import matplotlib.pyplot as plt
import numpy as np

halfCarLength = 0.2
vehicle1 = (3, 0.075) #(pi1=initialPosition, v1=calculatedVelocity)
vehicle2 = (0, 0.2) #(pi1=initialPosition, v1=calculatedVelocity)

time = np.arange(0, 40, 1)

#position of front of vehicle with respect to time
vehicle1Position_1 = time*vehicle1[1] + vehicle1[0]+halfCarLength
vehicle2Position_1 = time*vehicle2[1] + vehicle2[0]+halfCarLength

#position of back of vehicle with respect to time
vehicle1Position_2 = time*vehicle1[1] + vehicle1[0]-halfCarLength
vehicle2Position_2 = time*vehicle2[1] + vehicle2[0]-halfCarLength

#collideTime = (vehicle2[0]-vehicle1[0])/(vehicle1[1]-vehicle2[1])
#collidePosition = vehicle1[1]*collideTime + vehicle1[0]

#plotting the upper and lower position line for every vehicle
plt.plot(time, vehicle1Position_1, color='b', alpha=0.1)
plt.plot(time, vehicle2Position_1, color='r', alpha=0.1)
plt.plot(time, vehicle1Position_2, color='b', alpha=0.1)
plt.plot(time, vehicle2Position_2, color='r', alpha=0.1)

#filling the area between the two lines for each vehicle
plt.fill_between(time, vehicle1Position_1, vehicle1Position_2, alpha=0.4, color='b')
plt.fill_between(time, vehicle2Position_1, vehicle2Position_2, alpha=0.4, color='r')

#limiting the plot the the collision zone (where the vehicles should not collide)
plt.ylim(4.75,5.25)

plt.title("Collision Zone")
plt.xlabel("Time (s)")
plt.ylabel("Position (m)")

#print(collidePosition)