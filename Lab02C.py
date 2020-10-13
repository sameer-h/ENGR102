#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
By submitting this assignment , I agree to the following :
"Aggies do not lie , cheat , or steal , or tolerate those who do ."
"I have not given or received any unauthorized aid on this assignment ."

Names: Sameer Hussain

ENGR 102 - 214

Professor: Dr.Socolofsky
Assignment: Lab 02b
Date: 09/04/2019
shussain2@tamu.edu
Script: Labo02bIdealGas.py
Individual Lab


"""

print("In this program I will use the ideal gas formula PV = nRT in order to find the number of atoms of helium in a specific balloon")
print("I will be using absolute units for pressure and temperature as well as Helium's mass - 4.02 amu")
print("\n We're given pressure in 1.0473 bar, Temp of 98 degree C, Volume of 40cm - +- 5 percent error")

pressure_bar = 1.0473
#Bar to pascal = bar * 100000
pressure = 104730.0 #in pascals
temp = 371.15 #98+273.15 
volume = 40.0
volfiveplus = 42.0 #+5% 
volfiveminus = 38.0 #-5%

avagadro_cst = (6.02214076*10**23)

r_cst = 8.31432

print("\nTo find atoms we need to find 'n' which is the moles of helium in balloon")

n = ((pressure * volume) / (r_cst * temp))

n_plusfive = ((pressure * volfiveplus) / (r_cst * temp))

n_minusfive = ((pressure * volfiveminus) / (r_cst * temp))

#Finding number of atoms from each mol

atm_plusfive = (n_plusfive * avagadro_cst)

atm_minusfive = (n_minusfive * avagadro_cst)

atm = (n * avagadro_cst)

print("\nThe number of helium atoms in 40cm balloon is", atm, "atoms")
print("Now with +5% error volume it is", atm_plusfive, "atoms. \nWith -5% error volume it is", atm_minusfive, "atoms")








