#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
By submitting this assignment , I agree to the following :
"Aggies do not lie , cheat , or steal , or tolerate those who do ."
"I have not given or received any unauthorized aid on this assignment ."

Names: Sameer Hussain

ENGR 102 - 214

Professor: Dr.Socolofsky
Assignment: Lab 02b
Date: 09/04/2019
shussain2@tamu.edu
Script: Labo02bTrig.py
Individual Lab

Using PV = nRT (Ideal Gas Formula) to find the number of atoms of helium in a 40cm balloon and also accounting for error rates.


"""

from math import *

print("In this first part of the program angle in degrees is converted to radians and revolutions")
# Converting Radians to Degrees
angle = 700.0 #in degrees
revolutions = floor((angle / 360)) #floor so we can find the remainder or radians
rads = radians((angle % 360)) #modulo for remainder of radians

print("From the original angle is", angle)
print("Revolutions is", revolutions, "and radians are", rads)


original_angle = ((revolutions * 360) + degrees(rads))

print("The original angle is", original_angle, "degrees")



######

print("\nIn this part we are manipulating the atan2 function to be on 0<theta<2pi scale")

x = -0.78453  #Two negatives - works
y = -1
#print(atan(x/y))

f = ((atan2(y,x) + (2*pi)) % (2*pi))
print("\nTwo negatives (3rd quad)",f)

x = 0.3789  #Y negative - works
y = -0.89

f = ((atan2(y,x) + (2*pi)) % (2*pi))  
print("\n Y neg(4th quad)",f)

x = -0.24789 #X negative - works
y = 0.68

f = ((atan2(y,x) + (2*pi)) % (2*pi))
print("\n X neg(2nd Quad)",f)


x = 0.78453  #Both positive - works
y = 1

f = ((atan2(y,x) + (2*pi)) % (2*pi))
print("\nBoth positive(1st Quad)",f)


##### Trying at different values
x = 12.0
y = -3.9
lhs = sin(x+y)
rhs = sin(x)*cos(y) + cos(x)*sin(y)
print("\n LHS:", lhs)
print("RHS:", rhs)
z = lhs - rhs
print("The difference is", z)

# Minimal change
x = -0.23
y = 0.64
lhs = sin(x+y)
rhs = sin(x)*cos(y) + cos(x)*sin(y)
print("\n LHS:", lhs)
print("RHS:", rhs)
z = lhs - rhs
print("The difference is", z)

# Minimal change
x = 0.23
y = -0.64
lhs = sin(x+y)
rhs = sin(x)*cos(y) + cos(x)*sin(y)
print("\n LHS:", lhs)
print("RHS:", rhs)
z = lhs - rhs
print("The difference is", z)


# Minimal change
x = -10.2
y = -12.2
lhs = sin(x+y)
rhs = sin(x)*cos(y) + cos(x)*sin(y)
print("\n LHS:", lhs)
print("RHS:", rhs)
z = lhs - rhs
print("The difference is", z)

#Conclusion on trig identity

print("\nAs we can see there are minimal differences, and the identity proves to be true")
print("One could suspect that in Quadrant 3, (only tan is +) sin and cos are not positive and python may mess up their values")
print("But from all these values, the trig identity proves to be true in all these different cases")














