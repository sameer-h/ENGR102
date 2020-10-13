#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 15:17:35 2019

@author: sameerhussain

Solve for the area of a sphere

ENGR 102 - 214

Professor: Dr.Socolofsky

Date: 09/04/2019
shussain2@tamu.edu

"""

from math import pi

def sphere_area(rad):
    """
    Compute the area of a sphere of radius rad
    
    """
    
    #Compute area of a sphere in squae units compatible with input
    
    A = 4. * pi * rad**2
    
    return (A)


def sphere_vol(rad):
    """
    Compute the volume of a sphere in cubic units
    
    """
    
    #Compute area of a sphere in squae units compatible with input
    
    vol = 4./3. * pi * rad**3
    
    return (vol)






#Pre processor
print("This program calculates the area of a sphere from given input")
r = float(input("Enter the radius in meters      ")) # radius in meters

#Processor -- do not edit below this line ----------------------------

area = sphere_area(r)
V = sphere_vol(r)

#print("Area of sphere is", area, "from radius", r)
print("\nThe area and volume of a sphere of radius %.3f" % r)
print(' area = %.2f, volume = %.2f' % (area, V))


