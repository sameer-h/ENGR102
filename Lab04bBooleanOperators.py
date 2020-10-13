#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 16:43:14 2019

By submitting this assignment , I agree to the following :
"Aggies do not lie , cheat , or steal , or tolerate those who do ."
"I have not given or received any unauthorized aid on this assignment ."

Names: Sameer Hussain

ENGR 102 - 214

Professor: Dr.Socolofsky
Assignment: Lab 02b
Date: 09/22/2019
shussain2@tamu.edu
Script: Labo04bBooleanOperators.py
Individual Lab

Boolean Operators using logic statements and if/else
"""

#Function to convert string input from user to boolean expression

def convert_answer(answer):
    if answer == "True":
        ua = True
    elif answer == "False":
        ua = False
    else:
        return "Not a true/false bool value"
    return(ua)
    
# user input a, b, c values
    
a = convert_answer(input("Enter your boolean value for a   "))

b = convert_answer(input("Enter your boolean value for b   "))

c = convert_answer(input("Enter your boolean value for c   "))

guess = convert_answer(input("\nGuess for expression a and b and c    "))
if guess == a and b and c:
    print("Correct answer")
else:
    print("Incorrect")

guess = convert_answer(input("\nGuess for expression a or b or c     "))

if guess == a or b or c:
    print("Correct answer")
else:
    print("Incorrect guess")
    
guess = convert_answer(input("\n (not (a and not b) or (not c and b)) and (not b) or (not a and b and not c) or (a and not b)   "))

if guess == (not (a and not b) or (not c and b)) and (not b) or (not a and b and not c) or (a and not b):
    print("Correct answer")
else:
    print("Incorrect guess")
    
guess = convert_answer(input("\n (not ((b or not c) and (not a or not c))) or (not (c or not (b and c))) or (a and not c) and (not a or (a and b and c) or (a and ((b and not c) or (not b))))    "))

if guess == (not ((b or not c) and (not a or not c))) or (not (c or not (b and c))) or (a and not c) and (not a or (a and b and c) or (a and ((b and not c) or (not b)))):
    print("Correct answer")
else:
    print("Incorrect guess")
    
#Simplifying the last two expressions
    
guess = convert_answer(input("\nGuess for expression (not a and not c) or not b "))

if guess == (not a and not c) or not b:
    print("Correct answer")
else:
    print("Incorrect guess") 

guess = convert_answer(input("\nGuess for expression a or (not b and c) "))

if guess == a or (not b and c):
    print("Correct answer")
else:
    print("Incorrect guess")



