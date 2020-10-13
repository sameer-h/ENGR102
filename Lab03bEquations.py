#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 14:59:04 2019

By submitting this assignment , I agree to the following :
"Aggies do not lie , cheat , or steal , or tolerate those who do ."
"I have not given or received any unauthorized aid on this assignment ."

Names: Sameer Hussain

ENGR 102 - 214

Professor: Dr.Socolofsky
Assignment: Lab 02b
Date: 09/04/2019
shussain2@tamu.edu
Script: Labo03bEquations.py
Individual Lab

Computing Engineeing Formulas with user-defined functions

"""
#Pre processor

from math import *


def shear_stress(normal_stress, inter_fric, cohesion):
    
    shear = normal_stress * tan(radians(inter_fric)) + cohesion
    
    return(shear)
    
    
def kinetic_energy(mass, velocity):
    
    kinetic = (1/2) * mass * (velocity**2)
    
    return(kinetic)
    
def reynolds_num (fluid_velocity, chara_linear_dimen, kin_vis):
    
    reynolds = ((fluid_velocity * chara_linear_dimen)/kin_vis)
    
    return(reynolds)
    
def production (initial_rate, empirical_const, initial_decline, days):
    
    prod = (initial_rate/(1+(empirical_const*initial_decline*days)**(1/empirical_const)))
    
    return(prod)
 

#Processor
    
print("\nIn this program the user can enter in values to solve for a number of engineering equations")
print("\nFirstly, beginning with shear stress, individual values should be entered by the user")


normal_stress = float(input("Enter the normal stress in newtons:    "))
inter_fric = float(input("Enter internal friction newtons:   "))
cohe = float(input("Finally enter cohesion force:   "))
    
shear = shear_stress(normal_stress, inter_fric, cohe)

print("From your values, the shear stress is", shear)


print()

print("Kinetic energy")
mass = float(input("Enter the mass in g:    "))
velocity = float(input("Enter the velocity in m/s:     "))
kin = kinetic_energy(mass, velocity)
print("The kinetic energy from your values is", kin, "Joules")


print()

print("Reynolds Number")
fluid_velocity = float(input("Enter the fluid velocity in m/s:    "))
chara_linear_dimen = float(input("Enter character linear dimension in meters:   "))
kin_vis = float(input("Enter character kinematic viscosity in m^2/s:   "))
rey = reynolds_num(fluid_velocity, chara_linear_dimen, kin_vis)
print("The Reynolds number from your values is", rey)

print()

print("The production of oil")
initial_rate = float(input("Enter character initial rate in barrels:   "))
empirical_const = float(input("Enter the emipirical constant you want to use:   "))
initial_decline = float(input("Enter initial decline in barrels:   "))
days = float(input("Enter number of days:   "))
prod = production(initial_rate, empirical_const, initial_decline, days)
print("\n The production rate is", prod, "barrels of oi in total")
