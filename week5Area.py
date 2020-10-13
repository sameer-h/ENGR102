# -*- coding: utf-8 -*-
"""
By submitting this document, I agree to the following:
"Aggies do not lie, cheat, or steal, nor tolerate those who do."
"I have not given or recieved any unauthorized aid on this assignment."

Name: Kara Decker
 
Date: September, 23 2019
       
ENGR 102-214
Assignment: Computing the Area Under a Curve
Script: week5Area.py

This program will estimate the value of the area under a curve 
"""
import math

def v_t(t,g,m,c):
    """
    Calculates the value of v in the function v(t) = 2t
    
    """
    
    v = (g*m)/c * (1-math.exp((-c*t)/m))
        
    return(v)
    

#Pre-Processor
t0 = 0
tf = 30
n = int(input('Enter the number of segments:'))
g = 9.81
m = 81.7
c = 12.4

#Processor 
s = 0
ti = t0
err = 1.0e-6   
l = 1
while (abs(l-s))>err:
    l = s
    k = (tf-t0)/n
    while ti<tf:
        f1 = v_t(ti,g,m,c)
        f2 = v_t(ti+k,g,m,c)
        h = (f1+f2)/2
        r = h * k 
        s += r
        ti += k 
    n = 2*n

e = abs(l-s)
          
#Post-Processor
print('The final number of segments is:',n)
print('The final integral is:',s)
print('The approximation of the error is:',e)