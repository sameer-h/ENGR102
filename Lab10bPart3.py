#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 11:25:46 2019

@author: sameerhussain
"""

import numpy as np
import scipy.integrate as odeintx
import matplotlib.pyplot as plt

initial = 2560
# initial guess

def popvtime(y,t, k, ymax): #function for population vs time
    #growth = 0.026
   # maxp = 12000
    pop = k * (1-(y/ymax)) * y
    return pop

t = np.linspace(0, 100, 100) #creating a linspace for the plot

#p = odeint(popvtime, initial, t) #calling module and class

k = 0.026
y_max = 12000 #MAXIMUM Y VALUE

eq_n = odeint.odeint(popvtime, initial, t, args=(k, y_max))

yr = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50] #GIVEN DATA POINTS TO PLOT
pop = [2560, 2780, 3040, 3350, 3710, 4090, 4450, 4850, 5280, 5690, 6080]

plt.plot(eq_n, 'r-', label="World Population Growth") #plotting
plt.plot(yr, pop, 'bo', label='Measured Population')

plt.xlabel("Time (yrs)")

plt.ylabel("Population (persons)")

plt.title("Population vs Time")

plt.legend()

plt.show()