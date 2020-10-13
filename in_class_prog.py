#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 15:50:21 2019

@author: sameerhussain
"""
import numpy as np

from in_class import quad_eqn

coef = 1, 0, -1

from scipy.optimize import fsolve

xr = fsolve(quad_eqn, 2, args=coef)
print("The root of xr =", xr)

a, b, c = coef
xr = fsolve(quad_eqn, 2, args=(a, b, c))

#Integrate from 2 to 10

from scipy.integrate import quad
x0 = 2
x1 = 10
I = quad(quad_eqn, x0, x1, args=(1,0,-1))[0]

print("The integral from 2 to 10 of this quadratic equation is", I)

# Interpolation

x = np.linspace(2, 10, num=5)
f = quad_eqn(x, *coef)

#Create the interpolation object

from scipy.interpolate import interp1d
quad_interp = interp1d(x, f, kind='linear')

#Use quad interp to do interpolation
xp = np.linspace(2, 10, num=500)
fp = quad_interp(xp)

import matplotlib.pyplot as plt
plt.plot(x,f, 'bo')
plt.plot(xp, fp, 'g-')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend('f(x)', 'Interpolated f(x)')







