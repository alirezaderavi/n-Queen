#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 15:42:26 2022

@author: Alireza Deravi
"""

import numpy as np
import random as rnd

G=np.zeros([8,8])
ANS=np.zeros([8])
for i in range(0,8):
    ANS[i]=-1
Z=np.zeros([8,8])

# Initializing the assumed tree
def chess(index,A,G):
    G[index,A]=1
    for i in range(index+1,8):
        G[i,A]=-1


    point=A
    j=index+1
    while point>0 and j<8:
        G[j,point-1]=-1
        j=j+1
        point=point-1
    
    point=A
    j=index+1
    while point<7 and j<8:
        G[j,point+1]=-1
        j=j+1
        point=point+1
    return G


# Initializing the assumed tree
def chess1(ANS,G):
    j=0
    for j in range(0,8):
        if ANS[j]!=-1:
            A=int(ANS[j])
            chess(j,A,G)
      
    return G


tree=[
      [0,Z],[1,Z],[2,Z],[3,Z],[4,Z],[5,Z],[6,Z],[7,Z]
      ]
for p in range(0,8):
    ANS[0]=p
    bord=chess1(ANS,G)
    tree[0][1]=bord
    
    sart=True
    soton=True
    j=0
    k=0
    while sart==True:
        j=j+1
        i=0
        soton=True
        while soton==True:
            if k>50:
                True
            if tree[j-1][1][j][i]==0:
                ANS[j]=i
                G=np.zeros([8,8])
                tree[j][1]=chess1(ANS,G)
                soton=False
                #print(ANS)    baraye inke khoroji marahel moshakhas beshe
                #print(j)
                #print(tree[j][1])
            else:
                if i==7:
                    if ANS[j-1]==7:
                        tree[j][1]=np.zeros([8,8])
                        tree[j-1][1]=np.zeros([8,8])
                        j=j-2
                        i=int(ANS[j])
                        ANS[j]=-1
                        ANS[j+1]=-1
                        k=k+1
                        
                    else:
                        tree[j][1]=np.zeros([8,8])
                        j=j-1
                        i=int(ANS[j])
                        ANS[j]=-1
                    
            i=i+1
            if i==8:
                soton=False
        if j==7:
            sart=False
    print(ANS)
















