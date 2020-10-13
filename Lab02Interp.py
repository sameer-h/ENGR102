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
Script: Labo02bInterp.py
Individual Lab

Using linear interpolation in 3D space with x,y,z points

"""
print("In this programa we are calculating the linear intepolation using a 3D space")
print("The objective of this program is to test points in the T span of 13 to 84")
print("Below shoes T at different spans for 13 to 84 (interpolated values)")
print("\nTIME 50")
T = 50

#Point1

# x(T).
x0val = 1

x1val = 23

y0val = 13

y1val = 84

delX = x1val - x0val #slope

delT = y1val - y0val #slope pts

m_slope = delX / delT #slope formula for interpolation



x_val_output = x0val + (T - y0val) * m_slope #Interpolation equation
print("The X val is:")
print(str(x_val_output))

# Point 2 calculations 

# y(T)
ythirt = 3

yeighty = -5

y0val = 13

t_eighty = 84

delT = t_eighty - y0val

deltY = yeighty - ythirt

m_slope = deltY / delT


y_output_val = ythirt + (T - y0val) * m_slope
print("The Y val is:")
print(str(y_output_val))

# Output position of Z(T).
# Point 3 calculations 

# z(T)

z0val = 7

z1val = 10

y0val = 13

t_eighty = 84

delT = t_eighty - y0val

deltZ = z1val - z0val

m_slope = deltZ / delT

z_output_val = z0val + (T-y0val) * m_slope
print("The Z val is:")
print(str(z_output_val))


print("----------------------------------------------")
print("\nNOW TIME 49")
T = 49

#Point set 2

# x(T).
x0val = 1

x1val = 23

y0val = 13

y1val = 84

delX = x1val - x0val

delT = y1val - y0val

m_slope = delX / delT



x_val_output = x0val + (T - y0val) * m_slope
print("\nThe X val is:")
print(str(x_val_output))



#Y(T) value set


ythirt = 3

yeighty = -5

y0val = 13

t_eighty = 84

delT = t_eighty - y0val

deltY = yeighty - ythirt

m_slope = deltY / delT


y_output_val = ythirt + (T - y0val) * m_slope
print("The Y val is:")
print(str(y_output_val))

# Z(T) values


z0val = 7

z1val = 10

y0val = 13

t_eighty = 84

delT = t_eighty - y0val

deltZ = z1val - z0val

m_slope = deltZ / delT

z_output_val = z0val + (T-y0val) * m_slope
print("The Z val is:")
print(str(z_output_val))


print("--------------------------------------")
print("\nNOW TIME 48")
T = 48

#Point set 3

# x(T).
x0val = 1

x1val = 23

y0val = 13

y1val = 84

delX = x1val - x0val

delT = y1val - y0val

m_slope = delX / delT



x_val_output = x0val + (T - y0val) * m_slope
print("The X val is:")
print(str(x_val_output))



#Y(T) value set



ythirt = 3

yeighty = -5

y0val = 13

t_eighty = 84

delT = t_eighty - y0val

deltY = yeighty - ythirt

m_slope = deltY / delT


y_output_val = ythirt + (T - y0val) * m_slope
print("The Y val is:")
print(str(y_output_val))

# Z(T) point


z0val = 7

z1val = 10

y0val = 13

t_eighty = 84

delT = t_eighty - y0val

deltZ = z1val - z0val

m_slope = deltZ / delT

z_output_val = z0val + (T-y0val) * m_slope
print("The Z val is:")
print(str(z_output_val))

