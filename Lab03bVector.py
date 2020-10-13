#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 16:53:33 2019

By submitting this assignment , I agree to the following :
"Aggies do not lie , cheat , or steal , or tolerate those who do ."
"I have not given or received any unauthorized aid on this assignment ."

Names: Sameer Hussain

ENGR 102 - 214

Professor: Dr.Socolofsky
Assignment: Lab 02b
Date: 09/04/2019
shussain2@tamu.edu
Script: Lab03bVector.py
Individual Lab

This program performs vector operations from observer at 3D point to another point. Normalization, dot product, lines are part of the techniques used.

"""
#Pre processor

from math import *

def origin_pt(pt1, pt2):
    n_vector = pt2 - pt1
    
    return(n_vector)

def normali(vec1, vecmag):
    
    normal = (vec1 / vecmag)
    
    return(normal)
    
def mag(v1, v2, v3):
    m = sqrt(v1**2 + v2**2 + v3**2)
    
    return(m)

print("Start entering position values for observer, point A, and point B")

obsXpos = float(input("\n X position of observer: "))
obsYpos = float(input("Y position of observer: "))
obsZpos = float(input("Z position of observer: "))



pointAx = float(input("\nPoint A X position: "))
pointAy = float(input("Point A Y position: "))
pointAz = float(input("Point A Z position "))



pointBx = float(input("\nPoint B X position: "))
pointBy = float(input("Point B \"Y\" position: "))
pointBz = float(input("Point B \"Z\" position: "))



## We get the position if observer is at 0,0,0
# Point A
originAx = origin_pt(obsXpos, pointAx)
originAy = origin_pt(obsYpos, pointAy)
originAz = origin_pt(obsZpos, pointAz)
# Point B
originBx = origin_pt(obsXpos, pointBx)
originBy = origin_pt(obsYpos, pointBy)
originBz = origin_pt(obsZpos, pointBz)


# Magnitude of vector A
a_mag = mag(originAx, originAy, originAz)

# Magnitude of vector B
b_mag = mag(originBx, originBy, originBz)

# Normalizes  A
normAx = normali(originAx, a_mag)
normAy = normali(originAy, a_mag)
normAz = normali(originAz, a_mag)

# Normalizes B
normalizedBx = normali(originBx, b_mag)
normalizedBy = normali(originBy, b_mag)
normalizedBz = normali(originAz, b_mag)

# Dt product of vectors a and b

dpAB = (originAx * originBx) + (originAy * originBy) + (originAz * originBz)


# Magnitudes 
ab_combined = a_mag * b_mag


# Finding the angle
theta_rad = acos(dpAB / ab_combined)

# Converts angle in radians to degrees
theta_deg = degrees(theta_rad)

print("Dot product is", dpAB)

print("The angle of the observer from point A to point B is", theta_deg)
