#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
By submitting this assignment , I agree to the following :
"Aggies do not lie , cheat , or steal , or tolerate those who do ."
"I have not given or received any unauthorized aid on this assignment ."

Name: Sameer Hussain
    
    
ENGR 102 - 214

Professor: Dr.Socolofsky
Assignment: Lab 01b
Date: 08/28/2019
shussain2@tamu.edu
Script: Labo01b.py
Part 1 of individual Lab


"""

#https://www.allaboutcircuits.com/textbook/direct-current/chpt-2/voltage-current-resistance-relate/
#Ohms Law
amperes     =   5.0

ohms        =   20.0 #variables

voltage  = amperes * ohms

print('The voltage from ' ,amperes, 'amperes and ' , ohms, 'ohms is ' , voltage, ' volts') #print function

#https://www.chem.wisc.edu/deptfiles/genchem/netorial/modules/thermodynamics/energy/energy2.htm
#Kinetic energy formula
mass = 100.00
velocity = 2.0

kinetic_energy = (1/2) * mass * (velocity**2)

print('\n The Kinetic energy from' , mass, 'kg object at', velocity, 'm/s is ', kinetic_energy, 
      'Joules')

#Reynolds Number
#https://www.pinterest.com/pin/121737996156318879/
fluid_velocity = 0.5
kinematic_vis = 0.000001
chara_linear_dimen = 2.5

reynolds_num = ((fluid_velocity * chara_linear_dimen)/fluid_velocity)

print('\n The Reynolds Number from fluid velocity of' , fluid_velocity, 'm/s, kinematic viscosity of' , kinematic_vis, 'm^2/s, and characteristic linear dimension of ',chara_linear_dimen, 'm, the Reynolds number is', reynolds_num)

#Given through the assignment
#Arps Equation
initial_rate = 100
initial_decline = 2
empirical_const = 0.8
days = 20

production = (initial_rate/(1+(empirical_const*initial_decline*days)**(1/empirical_const)))
print('\nProduction from initial production rate', initial_rate, 'barrels per day, initial rate of decline of production of', initial_decline, 'barrles and constant of', empirical_const, ', ', days, 'days', ' to make production', production, 'barrels in total')

#Given through the assignment
#Mohr-Coulomb 
normal_stress = 20
cohesion = 2
inter_fric = 35

import math

shear_stress = normal_stress * math.tan(math.radians(inter_fric)) + cohesion
print('\nThe shear stress from normal stress', normal_stress, 'lbf/in^2 and internal friction angle of', inter_fric, 'degrees', ' and material cohesion of', cohesion, 'lbf/in^2 there is a shear stress of ' ,shear_stress, 'lbf/in^2')


