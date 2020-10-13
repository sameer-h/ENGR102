#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
By submitting this assignment , I agree to the following :
"Aggies do not lie , cheat , or steal , or tolerate those who do ."
"I have not given or received any unauthorized aid on this assignment ."

Name: Sameer Hussain
    
    
ENGR 102 - 214
Professor: Dr.Socolofsky
Assignment: Lab 01b Part 2
Date: 08/28/2019
shussain2@tamu.edu
Script: Labo01bPT2.py
Lab01b Part 2 - Evaluating Limits


"""
import math

#Evaluate f(x) = sin(x) / x
print ('This shows the evaluation of sin(x)/(x) near the limit x = 0.') #Introduction
print ('My guess for the analytical solution is ', '1 ')
x = 0.1 #Trying at larger value
fx = (math.sin(x)/x)
print ('The result evaluated at x = ', x , 'is ', fx )
x = 0.01 #Smaller value input
fx = (math.sin(x)/x)
print ('The result evaluated at x = ', x , 'is ', fx )
x = 0.00001 #Value that is even closer to 0
fx = (math.sin(x)/x)
print ('The result evaluated at x = ', x , 'is ', fx )  #Evaluation of limit
print ()


#Evaluate f(x) = 1-cos(x) / x^2
print ('This shows the evaluation of 1-cos(x)/(x)^2 near the limit x = 0.')
print ('My guess for the analytical solution is ', '1/2 ')
x = 0.1 #Larger value
fx = ((1 - math.cos(x))/(x*x))
print ('The result evaluated at x = ', x , 'is ', fx )
x = 0.01 #Smaller value
fx = ((1 - math.cos(x))/(x*x))
print ('The result evaluated at x = ', x , 'is ', fx )
x = 0.0001 #Value even closer to 0
fx = ((1 - math.cos(x))/(x*x))
print ('The result evaluated at x = ', x , 'is ', fx ) #Evaluation of limit
print ()

#Evaluate h(x) = (1 + (1/x))^x
print ('This shows the evaluation of h(x) = (1 + (1/x))^x near the limit x = infinity')
print ('My guess for the analytical solution is ', '2.72... or the value of e ')
x = 999 #Smaller value
fx = ((1 + (1/x))**x)
print ('The result evaluated at x = ', x , 'is ', fx )
x = 99999 #Larger value
fx = ((1 + (1/x))**x)
print ('The result evaluated at x = ', x , 'is ', fx )
x = 99999999999 #Value even closer to infinity
fx = ((1 + (1/x))**x)
print ('The result evaluated at x = ', x , 'is ', fx ) #Evaluation of limit
print ()
