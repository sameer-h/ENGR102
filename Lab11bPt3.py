#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 13:57:11 2019

By submitting this assignment , I agree to the following :
"Aggies do not lie , cheat , or steal , or tolerate those who do ."
"I have not given or received any unauthorized aid on this assignment ."

Names: Sameer Hussain

ENGR 102 - 214

Professor: Dr.Socolofsky
Assignment: Lab 11b
Date: 11/11/2019
shussain2@tamu.edu
Script: Labo011bPt3.py
Individual Lab

Aerodynamic Drag
"""
import scipy.optimize as opt

def aero(v,w,b,e,f,sigma):
    """
    computes the aero drag based on the equation
    
    """
    dp = (sigma/f)*(v**2)*391
    dl = 1245/(sigma*e)*(w**2/b)*(1/v**2)
    fov= dp-dl
    
    return(fov)


if __name__  == '__main__':
    w=15000.
    b=40.
    e=0.80
    f=4.
    sigma=0.533
    drag= opt.fsolve(aero, 0.1, args=(w,b,e,f,sigma)) #using scipy.optimize fsolve function with user defined function
    print("For a jet with weight", w, "lbs, a wingspan of ", b, ",ft, an efficiency ratio", e, " drag area of, ", f, "ft^2, and air density ratio of", sigma, " \n  the drag is", drag)