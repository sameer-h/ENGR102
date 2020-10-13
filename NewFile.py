#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 13:25:15 2019

@author: sameerhussain
"""
from math import *
import matplotlib.pyplot as plt
import numpy as np

def eq(z):
    y = ((12*(2**2))/6)*(1/(cos((2*z-32*0+0)**2)))
    return (y)

arr = []

for i in range(-3,4):
    x = eq(i)
    arr.append(x)


plt.xlabel("non-dimensional distance")
plt.ylabel("non-dimensional wave height")
plt.grid()
plt.title("Non-dimensional Wave Height vs Distance")
plt.plot(arr)


"""

for i in range(-3, 3, 0.75):
    x = eq(i)
    z_arr.append(x)

print(z_arr)
"""

z_arr = np.linspace(-3,3,8, endpoint=True)
print(z_arr)

y_arr = []

for i in z_arr:
    x = eq(i)
    y_arr.append(x)


print("\n\n", y_arr)

plt.plot(y_arr)
plt.legend("Analytical solution")
plt.show()


#Part 2 of the program

v = np.array([[1], [0]])
m = np.array([[1.00583, -0.087156], [0.087156, 1.00583]])
print(m)
#m = np.append(m, [[0.087156, 1.00583]], axis = 0)
i = 0
v1 = np.array([1])
v2 = np.array([0])

x = []
y = []
for i in range(250):
    x += [v[0]]
    y += [v[1]]
    v = m @ v
    

print(v)

plt.plot(x, y)
plt.title("Spiral Curve")
plt.xlabel("x-axis of points")
plt.ylabel("y-axis plotted")
plt.show()


    
    


