"""
By submitting this document, I agree to the following:
"Aggies do not lie, cheat, or steal, nor tolerate those who do."
"I have not given or recieved any unauthorized aid on this assignment."

Names: Sameer Hussain

ENGR 102 - 214

Professor: Dr.Socolofsky
Assignment: Lab 05b
Date: 09/18/2019
shussain2@tamu.edu
Script: Labo05bParachute.py
Individual Lab

Graphing and plotting with temperature
"""

import numpy as np
import matplotlib.pyplot as plt

temp = np.array([20.0,31.5,50.0,71.8,91.3])
res=np.array([761,817,874,917,1018])
max_x = 1100
min_x = 700
average=0
for a in res:
    average+=a
average/=len(res)
avg_x = average
for a in temp:
    average+=a
average/=len(temp)
avg_y = average

# Using the formula to calculate slope and intercept
numer = 0
denom = 0
for i in range(len(res)):
    numer += (res[i] - avg_x) * (temp[i] - avg_y)
    denom += (res[i] - avg_x) ** 2
slope = numer / denom
intercept = avg_y - (slope * avg_x)

# Calculating line values x and y
x = np.linspace(min_x, max_x, 1000)
y = intercept + slope * x


# Ploting Line
plt.plot(x, y, label='Regression Line')
# Ploting Scatter Points
plt.scatter(res, temp, label='Points')

plt.xlabel('Resistance (Ohms)')
plt.ylabel('Temperature (Celsius)')
plt.legend()
plt.show()

#Calculate St and Sr
st=0
sr=0
for count in range(5):
    st+=(temp[count]-avg_y)**2
    sr+=(temp[count]-intercept-slope*res[count])**2

print("R^2=",(st-sr)/st)

