#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 17:28:24 2019

By submitting this assignment , I agree to the following :
"Aggies do not lie , cheat , or steal , or tolerate those who do ."
"I have not given or received any unauthorized aid on this assignment ."

Names: Sameer Hussain

ENGR 102 - 214

Professor: Dr.Socolofsky
Assignment: Lab 05b
Date: 09/18/2019
shussain2@tamu.edu
Script: Labo05bIntegration.py
Individual Lab

Estimate the area under a curve using the Trapezoidal Rule
"""
from math import *


#Here, the function f(x) = 2t is made as a user defined function
def sumOf(x): 
      
    return ((2 * x)) 


def trapezoidal(t, g, m, c): 
      
    #Spacing
    h = (m - g) / c 
      
    # Computing sum of first and last terms from above
    s = (sumOf(g) + sumOf(m)) 
  
    #middle terms
    i = 1
    while i < c: 
        s += 2 * sumOf(m + i * h) 
        i += 1
          
    # h/2 = (b-a)/2n 
    return ((h / 2) * s) 
#RANGE OF INTEGRAL
x0 = 0
xn = 30
# Number of times/grid accuracy
c = int(input("Enter value of grids/times to compute:  "))

print ("Value of integral is ", trapezoidal(sumOf(x), x0, xn, c)) 