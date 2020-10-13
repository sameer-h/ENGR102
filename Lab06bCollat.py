#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 13:19:15 2019

Names: Sameer Hussain

ENGR 102 - 214

Professor: Dr.Socolofsky
Assignment: Lab 05b
Date: 09/18/2019
shussain2@tamu.edu
Script: Labo06bCollatz.py
Individual Lab

Python implementation of the Collatz Conjecture
"""
temp = []

def collatz(n):
    while n > 1:
        print(n, end=' ')
        if (n % 2):
            # n is odd
            n = 3*n + 1
            temp.append(n)
        else:
            # n is even
            n = n//2
            temp.append(n)
    print(1, end='')
 
 
n = int(input('Enter n: '))
print('Sequence: ', end='')
collatz(n)
print("\nIt took", len(temp), "iterations")