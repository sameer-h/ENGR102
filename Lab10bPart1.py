#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 03:11:49 2019

@author: sameerhussain
"""
import math
import matplotlib.pyplot as plt
from scipy import integrate
#import scipy.stats
import numpy

sig = 12.4
mew = 73.4
x = 90 #for 90%

def gauss(x, sd, mu):
    fx = (1/(sd*math.sqrt(2*math.pi))) * (math.exp((-(x-mu)**2)/(2*sd**2)))
    return (fx)

dx = lambda x: (1/(sig*math.sqrt(2*math.pi))) * (math.exp((-(x-mew)**2)/(2*sig**2)))

pts = []

for i in range(101):
    pts.append(gauss(i, sig, mew))

print(pts)

plt.plot(pts)
plt.xlim(0,105)
plt.show()

print("Yes this is a reasonable distribution to represent grades as there is a distinct, appropriate mean and scores that are centered around a normal distribution bell curve")


#integration from 2 places

def gauss_integrate(x):
    v = gauss(x, sig, mew)
    return v

x1 = mew + sig
x2 = mew + 2.0 * sig

#res = quad(gauss(), x1, x2)
#print("Integration from {} and {} -->".format(x1,x2), res)
#x2 = lambda x: x**2
#r = integrate.quad(x2, 0, 4)[0]
#print(r)
res1 = integrate.quad(dx, -numpy.inf, 90)[0]
err = integrate.quad(dx, -numpy.inf, 90)[1]
ans1 = 1-res1
#print(res1, res2, ans1, ans2)
print("\nThe probability of scoring 90% is", ans1)

students = (ans1 * 48) //1
print("In class of 48 students, ", students, " students will score above a 90")

#ans = 1-res1
#print("The probability of scoring a 90% is", ans)


