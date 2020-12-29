import time 
from math import *
import turtle
L=[0]*7
D=[[0]*6 for i in range (6)]
for i in range(0,7):
    # taking the coordinates of the points
    L[i]=[float(input("entrer l'abcisse du point "+str(i)+" : ")),float(input("entrer l'ordonné du point "+str(i)+" : "))]  # les cordonées des points
t_0=time.clock()
def distance(A,B):
    d=((A[0]-B[0])**2+(A[1]-B[1])**2)**(1/2)
    return d
for j in range (len(L)-1):
    for i in range (j+1,len(L)):
        D[j][(i-1)]= distance(L[j],L[i]) 
d_1=D[0][0]+D[1][1]+D[2][2]+D[3][3]+D[4][4]+D[5][5] # Initialization
F=[[L[0],L[1]],[L[1],L[2]],[L[2],L[3]],[L[3],L[4]],[L[4],L[5]]] 
C=F         
t_c=d_1
D_s=[[0]*6 for i in range (6)]
for p_0 in range (len(L)):
    for p_1 in range (len(L)):
        for p_2 in range (len(L)):
            for p_3 in range (len(L)):
                for p_4 in range (len(L)):
                    for p_5 in range (len(L)):
                        for p_6 in range (len(L)):   # Permutation 
                            if p_6!=p_5 and p_6!=p_4 and p_6!=p_3 and p_6!=p_2 and p_6!=p_1 and p_6!=p_0 and p_5!=p_4 and p_5!=p_3 and p_5!=p_2 and p_5!=p_1 and p_5!=p_0 and p_4!=p_3 and p_4!=p_2 and p_4!=p_1 and p_4!=p_0 and p_3!=p_2 and p_3!=p_1 and p_3!=p_0 and p_2!=p_1 and p_2!=p_0 and p_1!=p_0 :   
                               N=[L[p_0],L[p_1],L[p_2],L[p_3],L[p_4],L[p_5],L[p_6]]
                               for j in range (len(L)-1):
                                    for k in range (j+1,len(L)):
                                       D_s[j][k-1]= distance(N[j],N[k]) #calculate distances
                               for a_0 in range (len(D_s)): 
                                   for b_1 in range (1,len(D_s)):
                                      for c_2 in range (2,len(D_s)):
                                         for d_3 in range (3,len(D_s)):
                                            for e_4 in range (4,len(D_s)):
                                                    s_2=D_s[0][a_0]+D_s[1][b_1]+D_s[2][c_2]+D_s[3][d_3]+D_s[4][e_4]+D_s[5][5]
                                                    if s_2<=t_c :
                                                       t_c=s_2
                                                       C=[a_0,b_1,c_2,d_3,e_4,5]
                                                       P=[L[p_0],L[p_1],L[p_2],L[p_3],L[p_4],L[p_5],L[p_6]]  


t_f=time.clock()
# Show Result
print("le plus court chemin est : ",[[P[0],P[C[0]+1]],[P[1],P[C[1]+1]],[P[2],P[C[2]+1]],[P[3],P[C[3]+1]],[P[4],P[C[4]+1]],[P[5],P[C[5]+1]]])
print("la plus coutre distance est : " ,t_c)
print("le temps de l'execution est : " ,t_f-t_0)
V=[[P[0],P[C[0]+1]],[P[1],P[C[1]+1]],[P[2],P[C[2]+1]],[P[3],P[C[3]+1]],[P[4],P[C[4]+1]],[P[5],P[C[5]+1]]]