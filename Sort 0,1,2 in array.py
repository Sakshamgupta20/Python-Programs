# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 12:51:58 2019

@author: Saksham
"""

for _ in range(int(input())):
    n=int(input())
    x=list(map(int,input().split()))
    m=0
    h=n-1
    lo=0
    while(m<=h):
        if(x[m]==0):
            temp=x[m]
            x[m]=x[lo]
            x[lo]=temp
            lo+=1
            m+=1
        elif(x[m]==1):
            m+=1
        elif(x[m]==2):
            temp=x[m]
            x[m]=x[h]
            x[h]=temp
            h-=1
    print(x)
    print()