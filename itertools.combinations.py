# -*- coding: utf-8 -*-
"""
Created on Tue May 21 17:22:13 2019

@author: Saksham
"""

"""
You are given a string S. 
Your task is to print all possible size k replacement combinations of the string in lexicographic sorted order.
"""
from itertools import combinations_with_replacement
a,b=input().split()
a=sorted(a)
x=list(combinations_with_replacement(a,int(b)))
for i in x:
    print(''.join(i))
