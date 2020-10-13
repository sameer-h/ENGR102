# -*- coding: utf-8 -*-
"""
By submitting this document, I agree to the following:
"Aggies do not lie, cheat, or steal, nor tolerate those who do."
"I have not given or recieved any unauthorized aid on this assignment."

Names: Sameer Hussain

ENGR 102 - 214

Professor: Dr.Socolofsky
Assignment: Lab 05b
Date: 09/18/2019
shussain2@tamu.edu
Script: Labo05bParachute.py
Individual Lab

Estimate the area under a curve using the Trapezoidal Rule and solving a Parachute Problem
"""
import math

def parachute(t,g,m,c):
    
    v = (g*m)/c * (1-math.exp((-c*t)/m)) #User defined function for the parachute problem
        
    return(v)
    #Pre-Processor
t0 = 0
tf = 30
segments = int(input('Enter the number of segments:'))
g = 9.81
m = 81.7
c = 12.4

#Error and Tolerance
err = 1.0e-6   
z = 1
s = 0
while (abs(z-s))>err: #Outside loop for segments from user
    z = s
    s = 0
    ti=t0
    k = (tf-t0)/segments
    while ti<tf: #Inside loop for the calculation and 2 factor
        f1 = parachute(ti,g,m,c)
        f2 = parachute(ti+k,g,m,c)
        h = (f1+f2)/2
        r = h * k 
        s += r
        ti += k 
    segments = 2*segments

error_rate = abs(z-s)
          

print('The final number of segments is:',segments)
print('The final integral is:',s)
print('The approximation of the error is:',error_rate)