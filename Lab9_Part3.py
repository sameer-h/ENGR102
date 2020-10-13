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
Script: Labo09bPart3.py
Individual Lab

Weather Data and Plot
"""
import matplotlib.pyplot as plt

f=open("WeatherDataMac.csv") #Weather data open
data=f.read().splitlines()
print("Date",end='')
print("Max Temp".rjust(20),end='')
print("Min Temp".rjust(15))

for dat in data[1:]:
    da=dat.split(',')
    print(da[0],end='')
    print(da[1].rjust(10),end='')
    print(da[3].rjust(15))

print("\n\n\n\n")

print("Date","Precipitation".rjust(20))

precip=0

for dat in data[1:]:
    da=dat.split(',')
    print(da[0],end='')
    print(da[-1].rjust(8))
    precip+=float(da[-1])
    #Averaging
print("The average precipitation over the three years is",round(precip/(len(data)-1),3),"inches")

print("\n\n\n\n")

max,min,max_day,min_day=-99999,99999,'',''
press_inc,press_dec,last_press=0,0,30.25
humid_days=0

for dat in data[1:]:
    da = dat.split(',')
    if int(da[1])>max:
        max=int(da[1])
        max_day=da[0]
    if int(da[3])<min:
        min=int(da[3])
        min_day=da[0]
    if float(da[-3])<last_press:
        press_dec+=1
    elif float(da[-3])>last_press:
        press_inc+=1
    last_press=float(da[-3])
    if float(da[8])>=90:
        humid_days+=1
        #Varibles for weather
print("Max Temp recorded was",max,"on",max_day)

print("Min Temp recorded was",min,"on",min_day)

print("Average pressure increased day over day",press_inc,"times")

print("Average pressure decreased day over day",press_dec,"times")

print("The number of days with average humidity at or greater than 90 is",humid_days,'days')

print("Thus, ",round((humid_days/(len(data)-1))*100,2),'% of days has an average humidity of 90% or greater',sep='')

print("Pick one to plot:")

[print(a,end='\t') for a in data[0].split(',')]
to_plot=input('\n')
num=data[0].split(',').index(to_plot)



x=[b for b in range((len(data)-1))]

y=[]

for d in data:
    y.append(d.split(',')[num])
y=y[1:]

plt.scatter(x, y, label='Points')

plt.xlabel('Days since 1/1/2015') #Plotting

plt.ylabel(to_plot)

plt.legend()

plt.show()
