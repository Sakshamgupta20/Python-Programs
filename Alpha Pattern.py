# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 16:35:57 2019

@author: Saksham
"""

"""
printing pattern
"""
import string
alpha = string.ascii_lowercase
n=26
L=[]
for i in range(n):
    s = "-".join(alpha[i:n])
    L.append(s[::-1]+s[1:])
width = len(L[0])
for i in range(len(L)-1,0,-1):
    print(L[i].center(width,'-'))
for i in range(0,len(L)):
    print(L[i].center(width,'-'))