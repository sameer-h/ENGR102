#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 13:57:11 2019

By submitting this assignment , I agree to the following :
"Aggies do not lie , cheat , or steal , or tolerate those who do ."
"I have not given or received any unauthorized aid on this assignment ."

Names: Sameer Hussain

ENGR 102 - 214

Professor: Dr.Socolofsky
Assignment: Lab 11b
Date: 11/17/2019
shussain2@tamu.edu
Script: Labo12bPT1.py
Individual Lab

Drawing Tally Marks
"""

from turtle import *

up()
right(90)


forward(300)
left(180)


forward(600)
left(90)


forward(350)
left(90)

down()

def r_tally ():  #SINGLE DIGIT TALLY MARKS (1-4)

    #  Starting to do the tally
    forward(100)
    left(90)

    
    up()
    forward(30)
    
    
    left(90)
    forward(100)
    
    
    left(180)
    down()
    return

def s_tally ():
    right(50)
    forward(170)
    up()
    left(140)  
    forward(160)
    left(90)
    forward(110) # SLANTING TALLYMARK FOR EACH 5th TALLY MARK
    left(180)
    down()
    
def five_fun ():

    for i in range(4):
        r_tally()
    
    s_tally()

def tally_mark_setter(): #FOR THE WHOLE NUMBER OF TALLYMARKS
    for m in range(5):
        five_fun()

    up()
    
    forward(170)
    right(90)
    forward(750)
    left(90)
    down()
    
tal = int(input("Tallies to draw? You can enter uptill 100"))

for x in range(tal//25):
    tally_mark_setter() #TWENTY FIVE TIMES
    
tal2 = tal%25# GETTING THE REMAINDER OF TALLY MARKS TO DRAW

for y in range(tal2//5):
    five_fun()
    
tal3 = tal2%5 #BY FACTOR OF 5

for z in range(tal3): #REGULAR  TALLY  MARK
    r_tally()
        

done()  #Drawing window for viewing
