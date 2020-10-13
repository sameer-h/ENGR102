#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 17:59:59 2019

By submitting this assignment , I agree to the following :
"Aggies do not lie , cheat , or steal , or tolerate those who do ."
"I have not given or received any unauthorized aid on this assignment ."

Names: Sameer Hussain

ENGR 102 - 214

Professor: Dr.Socolofsky
Assignment: Lab 02b 
Date: 09/22/2019
shussain2@tamu.edu
Script: Labo04bMathPractice.py
Individual Lab

Generating a random number between 1 and 20 and doing subtraction problem, making sure that the difference is always positive.
"""

from random import *
#Pre Processor
def math_practice():
    a = randint(1,20)
    b = randint(1,20)
#While loop    
    while a - b < 0:
        a = randint(1,20)
        b = randint(1,20)
    #User answer   
    userans = int(input("Enter your guess for the problem " + str(a) + " - " + str(b) +  " = "))
    if userans == (a - b):
        print("You are correct!")
    else:wha
        print("That is incorrect! The correct answer is " + str(a-b))
#Post processor

math_practice()
    

