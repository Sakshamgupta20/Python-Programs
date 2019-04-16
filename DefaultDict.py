# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 22:32:02 2019

@author: Saksham
"""

"""
In this challenge, you will be given 2 integers, n and m. There are n words, which might repeat, in word group A. There are m words belonging to word group B. For each m words, check whether the word has appeared in group A or not. Print the indices of each occurrence of m in group A. If it does not appear, print -1.
"""

from collections import defaultdict
n1,n2=map(int,input().split())
A=defaultdict(list)
B=[]
for i in range(n1): A[input()].append(str(i+1))
for i in range(n2): B.append(input()) 

for i in B:
    if i in A.keys():
        print(' '.join(A[i]))
    else: print("-1")