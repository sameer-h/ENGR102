#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 15:30:28 2019

By submitting this assignment , I agree to the following :
"Aggies do not lie , cheat , or steal , or tolerate those who do ."
"I have not given or received any unauthorized aid on this assignment ."

Names: Sameer Hussain

ENGR 102 - 214

Professor: Dr.Socolofsky
Assignment: Lab 02b
Date: 09/22/2019
shussain2@tamu.edu
Script: Labo04bDiscont.py
Individual Lab

Computing Discontinuous Equations

In this program, the safe loading in pounds per square inch (lbs/in^2) is calculated from
the slimness ratio.
"""

def safe_loading(s):
    if s < 100.0:
        sl = 16500 - 0.475 * (s**2)
    elif s >= 100.0:
        sl = (17900/(2+(s**2)/17900))
    
    return(sl)

#a = safe_loading(101)

#print(a)
    
