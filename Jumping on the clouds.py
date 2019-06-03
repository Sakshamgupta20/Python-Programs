# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 15:52:48 2019

@author: Saksham
"""

def jumpingOnClouds(c, k):
    flag=1
    energy=100
    while(flag):
        for i in range(0,len(c),k):
            if(energy!=100 and i==0):
                flag=0
                break
            if(c[i]==0):
                energy-=1
            else:
                energy-=3
    return(energy)

jumpingOnClouds([0,0,1,0],2)