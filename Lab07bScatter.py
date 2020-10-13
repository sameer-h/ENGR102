#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 22:49:50 2019

Names: Sameer Hussain

ENGR 102 - 214

Professor: Dr.Socolofsky
Assignment: Lab 06b
Date: 09/18/2019
shussain2@tamu.edu
Script: Lab07bScatter.py
Individual Lab

Scatter plot
"""
import numpy as np
import matplotlib.pyplot as plt

pts = []
xlabels = input("What label for x axis?")
ylabels = input("\nWhat label for y axis?")

print("First point: ")

while True:
    xp = float(input("Input x coordinate: "))
    yp = float(input("Input y coordinate:  "))
    p = [xp, yp]
    pts.append(p)
    
    mp = input("Add another point? y/n ")
    
    if mp == "y":
        print("Next point: ")
    else:
        break

np.array(pts)

xpts = []
ypts = []

for i in range(0, len(pts)):
    xpts.append(pts[i][0])
    ypts.append(pts[i][1])
    

plt.plot(xpts, ypts, 'bo', linewidth = 1.0)

plt.xlabel(xlabels)
plt.ylabel(ylabels)
plt.grid()

plt.show()




    