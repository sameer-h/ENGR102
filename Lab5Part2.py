#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 12:28:17 2019

@author: sameerhussain
"""
#Pre processor
#Declaring varibales
temp = [97,99,99,100,99,100,99,99,96,95,94,94,96,99,96,97,89,87,89,92,92,93,94,94]
mins = temp[0]
maxs = temp[0]
#List for the error in the list
t_err = []
total_e = 0

#Function for finding the min and max values in the temperature list
def min_max(maxs,mins):
    for i in range(len(temp)):
        if temp[i] < mins: #iterating through the list and finding max, min
            mins = temp[i]
        if temp[i] > maxs: 
            maxs = temp[i]
    return(maxs,mins)

def sum_eq(temp): #Finding the average temperature in the list
    n = len(temp)
    y = 0
    total = 0
    for y in range(len(temp)):
        total += temp[y]
        avg = total/(n+1)
    return(avg)
  
def lreg(temp): #Linear regression using list values 
    sxy = 0 #Sum of x and y
    sx = 0 # Sum of x
    sy = 0 #Sum of y
    sx2 = 0 #Sum x^2
    
    for i in range (1, len(temp)): #Iterating through list
        sxy += (temp[i - 1] * i)
        sx += i #Summation
        sx2 += i**2
        sy += temp[i - 1]
        m = ((len(temp) * sxy) - (sx * sy)) / ((len(temp) * sx2) - sx**2) #Given equation
        
        y_avg = sum_eq(temp)
        x_avg = sx / len(temp)
        b = y_avg - (m * x_avg)
        return(m, b)
        
if __name__ == '__main__':
    
    y = min_max(maxs,mins)
    s = sum_eq(temp)
    print("\nThe max and min respectively are: ",y, " in degrees F")
    print("\nThe average is: ", s, " degrees F")
    
    
    #Expected temperature and the actual temperature 
    #Forecast
    
    for index in range(1, len(temp) - 1):
        t_err.append(abs((temp[index] - temp[index] + 1))) #Adds an item to the end of the list
    for i in t_err:
        total_e += i
        e_avg = (1 / len(temp)) * total_e
    print("\nAverage err in forcasting when assuming that the next days temp is today's temp is", e_avg)
    
    m = lreg(temp)[0]
    b = lreg(temp)[1]

    #Line of Best fit
    for i in range(1,10):
        tempf = (m * i) + b
        print("\nTemperature in" , i , " days is ", tempf, "degrees F")
        
    print("\nThe forecast is in disagreement with the normal climate trends for this time of the year as linear regression overestimates the values of temperature")