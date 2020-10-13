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

Probability of Random Events
"""


def facts(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i #factorial function
    return factorial


def exps(l):
    sum1 = 1 + l
    for i in range(2, 100): #Exponents
        sum1 = sum1 + ((l ** i) / facts(i))
    return sum1


def compute(n1, la=1): #Lambda
    return (exps(-la) * la ** n1) / facts(n1)


lam = float(input("Enter Lambda: "))

while True:
    a = input("Enter a value for n (or q to quit): ")
    if a.lower() == 'q': #quit or enter again
        break
        exit()
    print("P(n)=", compute(int(a), la=lam)) #function

