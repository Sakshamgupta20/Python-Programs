# -*- coding: utf-8 -*-
"""
Created on Fri May 31 13:42:41 2019

@author: Saksham
"""


def countingValleys(n, s):
    x=list(s)
    u=0
    d=0
    count=0
    for i in x:
        print(u,d,count)
        if(i=='U'):
            u+=1
        else:
            d+=1
        if(u==d and i=='U'):
            d=0
            u=0
            count=count+1
    print(count)

countingValleys(8,'DDUUDDUDUUUD')