# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 14:16:56 2019

@author: Saksham
"""

def beautifulDays(i, j, n):
    count=0
    for k in range(i,j+1):
        if(abs(k-(int(''.join(list(reversed(str(k)))))))%n)==0: count+=1
    return(count)
print(beautifulDays(20,23,6))