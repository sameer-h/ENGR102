"""
By submitting this document, I agree to the following:
"Aggies do not lie, cheat, or steal, nor tolerate those who do."
"I have not given or recieved any unauthorized aid on this assignment."

Names: Sameer Hussain

ENGR 102 - 214

Professor: Dr.Socolofsky
Assignment: Lab 09b
Date: 10/26/2019
shussain2@tamu.edu
Script: Labo09bPart1.py
Individual Lab

Converting Fahrenheit to Celsius
"""
f=open("Fahrenheit.dat") #Open file

temps=f.read().splitlines()

f.close()

f=open("Celsius.dat","w")

f.write("High Temperatures in September for College Station (C)")

for temp in temps: #Write values
    f.write(str((int(temp)-32)*5/9)+'\n')
f.close()