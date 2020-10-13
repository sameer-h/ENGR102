#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 15:12:11 2019

@author: sameerhussain
"""

import numpy as np
from random import *

temp = []
def wg(i):
    z = 0
    minv = int(input("Input min rate "))
    maxv = int(input("Input max rate "))
    x = randint(minv, maxv)
    
    for z in range(0, i):
        temp.append(randint(minv, maxv))
        
    return(temp)


i = int(input("How many days do you want this value calculated "))
wg(i)
print(temp)