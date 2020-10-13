#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 15:32:57 2019

Names: Sameer Hussain

ENGR 102 - 214

Professor: Dr.Socolofsky
Assignment: Lab 06b
Date: 09/18/2019
shussain2@tamu.edu
Script: Lab06b10Year.py
Individual Lab

Estimating the 10-year risk of a heart attack using the NHLBI guide
"""

def valueReturn(gender, smokes, bloodtr):
    if gender in ("Male", "MALE", "male"):
        sex = "male"
    if gender in ("Female", "FEMALE", "female"):
        sex = "female"

    if smokes in ("yes", "True", "Yes", True, 1):
        smoker = True
    if smokes in("no", "False", "No", False, 0):
        smoker = False
    
    if bloodtr in ("yes", "True", "Yes", True, 1):
        bloodtreat = True
    if bloodtr in ("no", "False", "No", False, 0):
        bloodtreat = False

    return(sex, smoker, bloodtreat)
"""  
a = valueReturn(**args)
mySex = a[0]
myX = a[1]
"""
# USER DEFINED FOR FINDING POINTS ON AGE 
def agePts(sex, age):
    points = 0
    if sex == "male":
          # Age - male        
        if  20 <= age <= 34:
            points-=9
        if  35 <= age <= 39:
            points-=4
        if  40 <= age <= 44:
            points-=0
        if  45 <= age <= 49:
            points+=3
        if  50 <= age <= 54:
            points+=6
        if  55 <= age <= 59:
            points+=8
        if  60 <= age <= 64:
            points+=10
        if  65 <= age <= 69:
            points+=11
        if  70 <= age <= 74:
            points+=12
        if  75 <= age <= 79:
            points+=13

    #IF FEMALES
    elif sex == "female":
        # Age - female        
        if  20 <= age <= 34:
            points-=7
        if  35 <= age <= 39:
            points-=3
        if  40 <= age <= 44:
            points-=0
        if  45 <= age <= 49:
            points+=3
        if  50 <= age <= 54:
            points+=6
        if  55 <= age <= 59:
            points+=8
        if  60 <= age <= 64:
            points+=10
        if  65 <= age <= 69:
            points+=12
        if  70 <= age <= 74:
            points+=14
        if  75 <= age <= 79:
            points+=16

    return(points)


def cholesterolPts(sex, age, total_cholesterol):
    points = 0
    if sex == "male":
        #Total cholesterol, mg/dL
        if  20 <= age <= 39:
            if total_cholesterol < 160:
                points +=0
            if 160 <= total_cholesterol <= 199:
                points+=4
            if 200 <= total_cholesterol <= 239:
                points+=7
            if 240 <= total_cholesterol <= 279:
                points+=9
            if total_cholesterol > 289:
                points+=11
        if  40 <= age <= 49:
            if total_cholesterol < 160:
                points +=0
            if 160 <= total_cholesterol <= 199:
                points+=3
            if 200 <= total_cholesterol <= 239:
                points+=5
            if 240 <= total_cholesterol <= 279:
                points+=6
            if total_cholesterol > 289:
                points+=8
        if  50 <= age <= 59:
            if total_cholesterol < 160:
                points +=0
            if 160 <= total_cholesterol <= 199:
                points+=2
            if 200 <= total_cholesterol <= 239:
                points+=3
            if 240 <= total_cholesterol <= 279:
                points+=4
            if total_cholesterol > 289:
                points+=5
        if  60 <= age <= 69:
            if total_cholesterol < 160:
                points +=0
            if 160 <= total_cholesterol <= 199:
                points+=1
            if 200 <= total_cholesterol <= 239:
                points+=1
            if 240 <= total_cholesterol <= 279:
                points+=2
            if total_cholesterol > 289:
                points+=3
        if  70 <= age <= 79:
            if total_cholesterol < 160:
                points +=0
            if 160 <= total_cholesterol <= 199:
                points+=0
            if 200 <= total_cholesterol <= 239:
                points+=0
            if 240 <= total_cholesterol <= 279:
                points+=1
            if total_cholesterol > 289:
                points+=1
# IF FEMALE
    elif sex == "female":
        if  20 <= age <= 39:
            if total_cholesterol < 160:
                points +=0
            if 160 <= total_cholesterol <= 199:
                points+=4
            if 200 <= total_cholesterol <= 239:
                points+=8
            if 240 <= total_cholesterol <= 279:
                points+=11
            if total_cholesterol > 289:
                points+=13
        if  40 <= age <= 49:
            if total_cholesterol < 160:
                points +=0
            if 160 <= total_cholesterol <= 199:
                points+=3
            if 200 <= total_cholesterol <= 239:
                points+=6
            if 240 <= total_cholesterol <= 279:
                points+=8
            if total_cholesterol > 289:
                points+=10
        if  50 <= age <= 59:
            if total_cholesterol < 160:
                points +=0
            if 160 <= total_cholesterol <= 199:
                points+=2
            if 200 <= total_cholesterol <= 239:
                points+=4
            if 240 <= total_cholesterol <= 279:
                points+=5
            if total_cholesterol > 289:
                points+=7
        if  60 <= age <= 69:
            if total_cholesterol < 160:
                points +=0
            if 160 <= total_cholesterol <= 199:
                points+=1
            if 200 <= total_cholesterol <= 239:
                points+=2
            if 240 <= total_cholesterol <= 279:
                points+=3
            if total_cholesterol > 289:
                points+=4
        if  70 <= age <= 79:
            if total_cholesterol < 160:
                points +=0
            if 160 <= total_cholesterol <= 199:
                points+=1
            if 200 <= total_cholesterol <= 239:
                points+=1
            if 240 <= total_cholesterol <= 279:
                points+=2
            if total_cholesterol > 289:
                points+=2
    
    return(points)

#FUNCTION FOR POINTS OF A SMOKER OR NON SMOKER
def smokerPts(smoker, age, sex):
    points = 0
    if sex == "male":
        if smoker:
            if 20 <= age <= 39:
               points+=8 
            if 40 <= age <= 49:
               points+=5
            if 50 <= age <= 59:
               points+=3
            if 60 <= age <= 69:
               points+=1
            if 70 <= age <= 79:
               points+=1 
        else: # nonsmoker
            points += 0
    elif sex == "female":
        if smoker:
            if 20 <= age <= 39:
               points+=9 
            if 40 <= age <= 49:
               points+=7
            if 50 <= age <= 59:
               points+=4
            if 60 <= age <= 69:
               points+=2
            if 70 <= age <= 79:
               points+=1 
        else:
            points += 0
    
    return(points)
# HDL CHOLESTEROL
def hdlPts(sex, hdl_cholesterol):
    points = 0
    if sex == "male":
        if hdl_cholesterol > 60:
            points-=1
        if 50 <= hdl_cholesterol <= 59:
            points+=0
        if 40 <= hdl_cholesterol <= 49:
            points+=1
        if hdl_cholesterol < 40:
            points+=2
    
    elif sex == "female":
        if hdl_cholesterol > 60:
            points-=1
        if 50 <= hdl_cholesterol <= 59:
            points+=0
        if 40 <= hdl_cholesterol <= 49:
            points+=1
        if hdl_cholesterol < 40:
            points+=2
            
    return(points)

def systolicPts(sex, bloodtreat, systolic_blood_pressure):
    points = 0
    if sex == "male":
        if not bloodtreat:
            if systolic_blood_pressure < 120:
                points+=0
            if 120 <= systolic_blood_pressure <= 129:
                points+=0
            if 130 <= systolic_blood_pressure <= 139:
                points+=1           
            if 140 <= systolic_blood_pressure <= 159:
                points+=1
            if systolic_blood_pressure >= 160:
                points +=2
        else: #if the patient is on blood pressure meds
            if systolic_blood_pressure < 120:
                points+=0
            if 120 <= systolic_blood_pressure <= 129:
                points+=1
            if 130 <= systolic_blood_pressure <= 139:
                points+=1           
            if 140 <= systolic_blood_pressure <= 159:
                points+=2
            if systolic_blood_pressure >= 160:
                points +=3
        
    elif sex == "female":
        if not bloodtreat: #NO BP MED
            if systolic_blood_pressure < 120:
                points+=0
            if 120 <= systolic_blood_pressure <= 129:
                points+=1
            if 130 <= systolic_blood_pressure <= 139:
                points+=2           
            if 140 <= systolic_blood_pressure <= 159:
                points+=3
            if systolic_blood_pressure >= 160:
                points +=4
        else: #YES BP MED
            if systolic_blood_pressure < 120:
                points+=0
            if 120 <= systolic_blood_pressure <= 129:
                points+=3
            if 130 <= systolic_blood_pressure <= 139:
                points+=4           
            if 140 <= systolic_blood_pressure <= 159:
                points+=5
            if systolic_blood_pressure >= 160:
                points +=6
                
    return(points)

 
if __name__ == "__main__":
    gender = input("Enter your gender as male or female: ")
    smokes = input("Enter yes or no if you are a smoker: ")
    bloodtr = input("Enter yes or no if you use blood pressure treatment: ")
    
    age = int(input("Enter your age from 20 to 79: "))
    
    vals = valueReturn(gender, smokes, bloodtr)
    sexgender = vals[0]
    smoke = vals[1]
    bloodtreatment = vals[2]
    
    agepoints = agePts(sexgender, age)
    
    totalch = int(input("Enter total cholesterol in mg/dl from 160 to 289: "))
    chopoints = cholesterolPts(sexgender, age, totalch)
    
    hdlch = int(input("Enter the hdl cholesterol you have from 40 to 60: "))
    
    sysb = int(input("Enter your systolic blood pressure in mmHg from 120 to over 160: "))
    
    smokepts = smokerPts(smokes, age, sexgender)
    
    hdlpoints = hdlPts(sexgender, hdlch)
    
    syspoints = systolicPts(sexgender, bloodtreatment, sysb)
    
    #prisk = (sexgender, agepoints, chopoints, smokepts, hdlpoints, syspoints)
    
    points = agepoints + smokepts + hdlpoints + syspoints + chopoints
    
    #points = apts + cpts + spts + hdlpts + syspts
    if sexgender == "male":
        if points <= 0:
            percent_risk ="<1%"
        elif points == 1:
            percent_risk ="1%"
        
        elif points == 2:
            percent_risk ="1%"
            
        elif points == 3:
            percent_risk ="1%"
            
        elif points == 4:
            percent_risk ="1%"
            
        elif points == 5:
            percent_risk ="2%"
            
        elif points == 6:
            percent_risk ="2%"
            
        elif points == 7:
            percent_risk ="2%"
            
        elif points == 8:
            percent_risk ="2%"
            
        elif points == 9:
            percent_risk ="5%"
            
        elif points == 10:
            percent_risk ="6%"
            
        elif points == 11:
            percent_risk ="8%"
            
        elif points == 12:
            percent_risk ="10%"
            
        elif points == 13:
            percent_risk ="12%"

        elif points == 14:
            percent_risk ="16%"
            
        elif points == 15:
            percent_risk ="20%"
            
        elif points == 16:
            percent_risk ="25%"
            
        elif points >= 17:
            percent_risk =">30%"
    
    elif sexgender == "female":
        if points <= 9:
            percent_risk ="<1%"
        elif 9 <= points <= 12:
            percent_risk ="1%"
        
        elif 13 <= points <= 14:
            percent_risk ="2%"
            
        elif points == 15:
            percent_risk ="3%"
            
        elif points == 16:
            percent_risk ="4%"
            
        elif points == 17:
            percent_risk ="5%"
            
        elif points == 18:
            percent_risk ="6%"

        elif points == 19:
            percent_risk ="8%"
            
        elif points == 20:
            percent_risk ="11%"
            
        elif points == 21:
            percent_risk ="14%"
            
        elif points == 22:
            percent_risk ="17%"

        elif points == 23:
            percent_risk ="22%"
            
        elif points == 24:
            percent_risk ="27%"
            
        elif points >= 25:
            percent_risk ="30%"
    
    print("Your ten year risk from your values is", percent_risk)
    
    
    
    
    
    
    
    
    
    
    
    