# -*- coding: utf-8 -*-
"""
Created on Mon May 27 14:26:47 2019

@author: Saksham
"""

"""
Atlelete Sort
"""
n,m=map(int,input().split())
x=[list(map(int,input().split())) for i in range(n)]
k=int(input())
x=sorted(x,key=lambda x: x[k])
for i in x:
    print(*i)