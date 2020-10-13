#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 15:24:41 2019

@author: sameerhussain
"""

#Compute e^(-x^2) using a MacLauren expansion

from math import factorial, exp

x = 0.05
tol = 1.e-8
err = 1.
n = 0
s = 0
def expand(x):
    while err > tol:
        new_term = (x**n / factorial(n))
        s = s + new_term
        err = new_term
        n = n + 1
    
    

x = float(input("Input the x value to calculate"))

print("exp(-%.3f^2) = %.3f " % (x,s))
print("The answer from math.exp() is: ", exp(-x**2))




