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
Script: Labo09bPart2.py
Individual Lab

Comma seperated Values
"""
name=input("What would you like to name your file?") #Naming fiel

prin=float(input("What is the loan amount?"))

i= float(input("What is the interest in a APY%?")) / 100

pay=float(input("What is the monthly payment?"))

f=open(name + '.csv', 'w') #Opening file

f.write("Month #,Beginning Balance,Interest,Ending Balance\n")
        
f.write("0,"+str(prin)+",0,"+str(prin)+"\n")

monthly= (prin / 12) * i

if pay<monthly: #Paying
    for n in range(1,60):
        f.write(str(n) +',' + str(prin) + ',' + str(monthly) + ',' + str(prin + monthly - pay) + '\n')
        prin= prin + monthly - pay
        monthly = (prin / 12) * i
else:
    n=1
    while prin>0:
        ending_balance= prin + monthly - pay
        if ending_balance<0:
            ending_balance=0
        f.write(str(n) + ',' + str(prin) + ',' + str(monthly) + ',' + str(ending_balance) + '\n')
        prin = ending_balance
        monthly = (prin / 12) * i
        n+=1
        
f.close()
