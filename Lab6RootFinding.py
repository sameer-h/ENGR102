#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 13:41:27 2019

@author: sameerhussain
"""

tol = 1.e-6

def func(ca,cb,cc,x): 
    return a*(x**3) + b*(x**2) + cc  


# Prints root of func(x) 
# with error of EPSILON 0
def bisection(a,b): 
  
    if (func(ca,cb,cc,a) * func(ca,cb,cc,b) >= 0):
        print("You have not assumed right a and b\n") 
        return
   
    c = a 
    while ((b-a) >= tol): 
  
        # Find middle point 
        c = (a+b)/2
   
        # Check if middle point is root 
        if (func(ca,cb,cc,c) == 0.0): 
            break
   
        # Decide the side to repeat the steps 
        if (func(ca,cb,cc,c)*func(ca,cb,cc,a) < 0): 
            b = c 
        else: 
            a = c 
              
    print("The value of root is : ","%.4f"%c) 


#def evenlyPrint(a,b)

def printVals(a,b):
    full = abs(a) + abs(b)
    iterations = (int(full) // 10)
    for i in range(a, b, iterations):
        print(func(ca,cb,cc,i), end=", ")


if __name__ == '__main__':

    ca = float(input("Enter the coefficient value of a:  "))
    cb = float(input("\nEnter the coeffic1ient value of b:  "))
    cc = float(input("\nEnter the coefficient value of c:  "))
#    x = float(input("Enter the x value to use : "))
    
    a = int(input("Enter the a value of interval : "))
    b = int(input("Enter the b value of interval : "))
    
    
    bisection(a, b)
    
    printVals(a,b)
    
    
    
