# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 12:30:30 2019

@author: Saksham
"""

def circularArrayRotation(a, k, queries):
    for i in range(k):
        a.insert(0,a.pop())
    return([a[i] for i in queries])

print(circularArrayRotation([1,2,3],2,[0,1,2]))