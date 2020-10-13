#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 16:41:37 2019

@author: sameerhussain
"""

from math import *
def x_t(x1, x0, t, t1, t0):
    """
    Compute the inteprolation of x_t
    
    """
    x_t = (x1 - x0) * ((t-t0)/(t-t0)) + x0
    
    
    
    # Problem #3
def P_N(lbs):
    
    e = lbs * 4.44822
    return (e)

lbs = float(input("Enter the amount of pounds    "))

x = P_N(lbs)

print("Newtons is", x)
 


