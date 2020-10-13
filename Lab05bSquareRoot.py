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
Assignment: Lab 05b
Date: 09/18/2019
shussain2@tamu.edu
Script: Labo05bSquareRoot.py
Individual Lab

Divide and average algorithm
"""
#Pre-Processor
from math import *

def squareRoot(a): 

		x = a 
		y = 1 #the guess we use with the epsilon
		e = 1.e-8
		while(x - y > e): #While tolerance to error
	
			x = (x + y)/2 #Formula for the square root
			y = a / x
	
		return(x) 

#Print statements

val = float(input("Enter in the number you want to calculate the square root of: "))

print("Square root of", val, "is", round(squareRoot(val), 9))