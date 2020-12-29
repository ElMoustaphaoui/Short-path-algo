import time 
from math import *
import turtle
L=[0]*7
D=[[0]*6 for i in range (6)]
for i in range(0,7):
    # taking the coordinates of the points
    L[i]=[float(input("entrer l'abcisse du point "+str(i)+" : ")),float(input("entrer l'ordonné du point "+str(i)+" : "))]  

