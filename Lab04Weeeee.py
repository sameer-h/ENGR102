#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 16:28:21 2019

@author: sameerhussain

By submitting this assignment , I agree to the following :
"Aggies do not lie , cheat , or steal , or tolerate those who do ."
"I have not given or received any unauthorized aid on this assignment ."

Name: Sameer Hussain
    
ENGR 102 - 214
Professor: Dr.Socolofsky
Assignment: Lab 04
Date: 09/18/2019
shussain2@tamu.edu
Script: Labo03Weather.py
This program outputs a statement about the quality of the weather based on the pollution index inputted by the user

"""

from math import *

#Pre processor

def classify(pollution_index):
    
    if pollution_index < 35.0:
        return "Based on the pollution index, the weather is pleasant"
    
    elif pollution_index >= 35.0 and pollution_index <= 65.0 :
        return "Based on the pollution index, the weather is unpleasant"
    
    elif pollution_index > 65.0 :
        return "Based on the pollution index, the weather is hazardous"
    
    return(-1)

    
#Post Processor    
pollution_index = float(input("Enter your pollution index for your area:   "))
print(classify(pollution_index))
    

        

