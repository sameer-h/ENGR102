#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 15:37:40 2019

@author: sameerhussain

This program computes the root of quadratic functionms

"""
from math import *


a = 2.0
b = 3.5
c = 6.

# Compute the discrminant

d = ((b**2) - 4. * a * c)
if d >= 0.:
    r = sqrt(d)
else:
    print("This is an imaginary root")
    r = sqrt(-d) * 1j
    print(r)
    
x1 = (-b + r) / (2 * a)
print("One root is", x1)
