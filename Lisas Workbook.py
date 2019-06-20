# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 11:54:12 2019

@author: Saksham
"""
import math
n,d=input().split()
d=int(d)
numbers=list(map(int,input().split()))
page=0
count=0
for i in numbers:
    t=1
    d1=d
    for j in range(math.ceil(i/d)):
        page+=1
        temp=[]
        for _ in range(d1):
            if(t<=i):
                temp.append(t)
                t+=1
        if(page in temp):
            count+=1
print(count)