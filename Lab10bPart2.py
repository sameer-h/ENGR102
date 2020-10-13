#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 11:22:37 2019

@author: sameerhussain
"""

#0.05 atm^(1/2) in I
#pt =3

def fn(x):
    f = (0.05 - (x/(1-x)) * (((6)/(2+x)) ** (1/2)))
    return f

from scipy.optimize import fsolve


#guess = 0.1
g = 0.1
x = fsolve(fn, g)
print(x)

