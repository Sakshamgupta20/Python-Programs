# -*- coding: utf-8 -*-
"""
Created on Fri May 31 14:54:53 2019

@author: Saksham
"""

def getMoneySpent(keyboards, drives, b):
    x=[]
    for i in keyboards:
        for j in drives:
            x.append(sum([i,j]))
    max=-1
    for i in x:
        if i>max and b >=i:
            max=i
    print(max)



getMoneySpent([3,1],[5,2,8],10)