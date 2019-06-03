# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 16:11:50 2019

@author: Saksham
"""

def findDigits(n):
    count=0
    for i in list(str(n)):
        try:
            if n%int(i)==0:
                count+=1
        except:
            continue
    return(count)
print(findDigits(1024))