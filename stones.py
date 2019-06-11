# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 12:21:23 2019

@author: Saksham
"""

def stones(n, a, b):
    res=set()
    for i in range(n):
        print(i)
        res.add((i*a)+b*(n-i-1))
    return(sorted(res))
    
print(stones(3,1,2))