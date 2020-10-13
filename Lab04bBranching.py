#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 16:02:42 2019

By submitting this assignment , I agree to the following :
"Aggies do not lie , cheat , or steal , or tolerate those who do ."
"I have not given or received any unauthorized aid on this assignment ."

Names: Sameer Hussain

ENGR 102 - 214

Professor: Dr.Socolofsky
Assignment: Lab 02b
Date: 09/18/2019
shussain2@tamu.edu
Script: Labo04bBranching.py
Individual Lab

Collects values for coefficients and determines wheter lines are parallel, perpendicular, or niether

"""
#User Inputs for variables
print("For the function ax+by = c and dx + ey = f")
a = float(input("Enter value of a:   "))
b = float(input("Enter value of b:   "))
c = float(input("Enter value of c:   "))
d = float(input("Enter value of d:   "))
e = float(input("Enter value of e:   "))
f = float(input("Enter value of f:   "))

#Setting up formulas for slope
slope1 = -a/b
slope2 = -d/e
eq1 = slope1 + c
eq2 = slope2 + f

if slope1 == slope2:
    print("Based on the slopes, the lines are parallel")

if eq1 == eq2 :
    print("The lines intersect")
    if slope1*slope2 == -1:
        print("The lines are also perpendicular")
elif slope1 != slope2 and eq1 != eq2: #Extra part I wanted to add
    print("None of the slopes are parallel/perpendicular and the lines don't intersect")








