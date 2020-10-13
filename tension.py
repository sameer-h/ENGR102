#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 20:00:00 2019

@author: sameerhussain
"""
from math import *

print("Problem #2")
tForce = 350
t1_angle = 65
t2_angle = 25
print("Total weight is", tForce, "Newtons.”
print(“First angle of tension force is", t1_angle, "degrees, and second is", t2_angle, "degrees.")
#T1 and T2 equal the system vector 0,350
#X comp of T1 and T2 = result
t1_y = tan((t1_angle * pi)/180)
t2_y = tan((t2_angle * pi)/180)

#Finding result by dividing the force by the added tangents of t1 and t2
res = (tForce / (t1_y + t2_y))

#res is back into equation to find T1 T2 components
tension1 = Matrix([-res, (tan((t1_angle*pi)/180)*res)])
tension2 = Matrix([res, (tan((t2_angle*pi)/180))*res])

print("Tension Force #1 is", tension1, ".")
print("Tension Force #2 is", tension2, ".")
print("Magnitude of T1 is", tension1.norm(), ".")
print("Magnitude of T2 is", tension2.norm(), ".")





print("Problem #2")
angle1 = radians(65)
angle2 = radians(25)
print("\nThe first tension has angle of 65 and second tension has angle of 25")
#Vector system of equations with Matricies
weight = Matrix([0, 350])
sys_eq = Matrix([[cos(angle1), -cos(angle2)], [sin(angle1), sin(angle2)]])
#Solving for the resultant vector - inverse res matrix * weight
resultant = Matrix(sys_eq.inv() * weight)

print("Tension in rope 1 is", round(resultant[0], 2), "Newtons"), 
print("Newtons and tension in rope 2 is", round(resultant[1], 2), "Newtons") 
#print("Tension Force #1 is", tension1, "N \n and Tension Force #2 is", tension2, "and magnitude of T1 is", tension1.norm(), "N \n and magnitude of T2 is", tension2.norm(), "N")
            
