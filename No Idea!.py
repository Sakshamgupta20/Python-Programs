# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 22:24:06 2019

@author: Saksham
"""

"""
There is an array of n integers. There are also 2 disjoint sets, A and B, each containing m integers. You like all the integers in set A and dislike all the integers in set B. Your initial happiness is 0. For each i integer in the array, if ,1 belongs to A you add 1 to your happiness. If ,i belongs to B you add -1 to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.
"""

n=input()
na=input().split()
A=set(input().split())
B=set(input().split())
sum=0
for i in na:
    if i in A:
        sum+=1
    if i in B:
        sum-=1
print(sum)