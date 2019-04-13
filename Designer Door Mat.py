# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 01:13:27 2019

@author: Saksham
"""

"""
Size: 7 x 21 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
"""

x=''
N, M = map(int,input().split())
for i in range(1,N,2): 
    y=(i * ".|.").center(M, "-")
    x=x+y+"\n"
x=x.rstrip("\n")
print(x)
print("WELCOME".center(M,"-"))
print(x[::-1])
    
    