#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
By submitting this assignment , I agree to the following :
"Aggies do not lie , cheat , or steal , or tolerate those who do ."
"I have not given or received any unauthorized aid on this assignment ."

Names: Sameer Hussain, Hayden Demny, Luke Karnei, Kiara Berry

ENGR 102 - 214

Professor: Dr.Socolofsky
Assignment: Lab 02
Date: 09/04/2019
shussain2@tamu.edu
Script: Labo02.py
Group Lab


"""

from math import *
#Objective print statements
print("Objective and Explanation")
print("In this program we are using linear interpolation on a sine curve - on the part that has the most curvature interval\n and picking 2 values and their components to estimate a third and also finding error")
print("\nFrom graph of sin \u03F4 we're using interpolation to dertermine step size on the interval")
print("pi/4 to 5pi/8")
print("\nThe initial angle for our interpolation will be pi/4 or 45 degrees")
print("on a range of pi/4 to 5pi/8")
print("the step size for the table will be pi/4")
print("We want to have an error percetange less than 20%")

#Variables

theta0 = (pi/4)
theta1 = ((5*pi)/8)
#d_t = (math.pi/2)
theta = (pi/3)
T = sin(theta)
y0 = sin(theta0)
y1 = sin(theta1)


#This set of equations is to find the true value of sin


lin_interp = (((theta-theta1)/(theta0-theta1))*y0) + (((theta-theta0)/(theta1-theta0))*y1)

print("\nThe linear interpolation of value pi/3 from values pi/4 and 5pi/8 and is the value", lin_interp)
print("The true value of sin theta is", T)
error = ((fabs(T-lin_interp))/T) * 100
print("The error percent for this is", error)


#2nd set of values

theta0 = (pi/4)
theta1 = ((5*pi)/8)
#d_t = (math.pi/2)
theta = (pi/2)
T = sin(theta)
y0 = sin(theta0)
y1 = sin(theta1)


#This set of equations is to find the true value of sin


lin_interp = (((theta-theta1)/(theta0-theta1))*y0) + (((theta-theta0)/(theta1-theta0))*y1)

print("\nThe linear interpolation of value pi/2 from values pi/4 and 5pi/8 and is the value", lin_interp)
print("The true value of sin theta is", T)
error = ((fabs(T-lin_interp))/T) * 100
print("The error percent for this is", error)

#Third set of values
theta0 = (pi/4)
theta1 = ((5*pi)/8)
#d_t = (math.pi/2)
theta = ((3*pi)/8)
T = sin(theta)
y0 = sin(theta0)
y1 = sin(theta1)


#This set of equations is to find the true value of sin


lin_interp = (((theta-theta1)/(theta0-theta1))*y0) + (((theta-theta0)/(theta1-theta0))*y1)

print("\nThe linear interpolation of value 3pi/8 from values pi/4 and 5pi/8 and is the value", lin_interp)
print("The true value of sin theta is", T)
error = ((fabs(T-lin_interp))/T) * 100
print("The error percent for this is", error)

# Best step size

print("\n The step size that we would use in a table would be in increments of pi/3.")
print("This is due to pi/3 having the lowest percentage of error of all the three values")



