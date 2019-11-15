# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 09:40:00 2019

@author: mjaa
"""

import matplotlib.pyplot as plt

plt.plot(-2, 7, 'ro')
plt.plot(2, 4, 'ro')
plt.plot(-4, -4, 'ro')
plt.plot(-8, -1, 'ro')
plt.plot([0, 0.6], [0, 0.8], 'r')

plt.plot(3, 0, 'bo')
plt.plot(9, -8, 'bo')
plt.plot(5, -11, 'bo')
plt.plot(-1, -3, 'bo')
plt.plot([0, -0.6], [0, 0.8], 'b')

slope = (4+4)/(2+4)

a = 1*slope

plt.plot(1, a, 'ro')

