# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 11:46:51 2019

@author: Saksham
"""

def jumpingOnClouds(c):
    i=0
    count=0
    while(i!=len(c)-1):
        try:
            if(c[i+1]==0 and c[i+2]==0):
                i=i+2
            elif(c[i+1]==0 and c[i+2]!=0):
                i=i+1
            elif(c[i+1]==1 and c[i+2]==0):
                i=i+2
            count+=1
        except:
            count+=1
            break
    return(count)
print(jumpingOnClouds([0,0,0,1,0,0]))