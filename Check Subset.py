# -*- coding: utf-8 -*-
"""
Created on Sat May 25 12:24:39 2019

@author: Saksham
"""

for i in range(int(input())):
    n1,a=input(),set(input().split())
    n2,b=input(),set(input().split())
    print(a.issubset(b))