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
Script: Labo11bPT1.py
Individual Lab

Prime Numbers
"""

def isPrime(n): #user defined function to determine  prime
    factors=[1]
    for i in range(2,n+1):
        if n%i==0:
            factors.append(i)
    return len(factors)!=1 and not len(factors)>2,factors

def isPosInt(b): #positive integer using .isnumeric()
    return b.isnumeric() and int(b)>0

while True:
    a=input("Enter a positive integer: ") 
    if a.lower()=='q':
        break
        exit() #exits if q is inputted
    elif isPosInt(a):
        print(isPrime(int(a))) #checking prime
    else:
        print("Try again")

