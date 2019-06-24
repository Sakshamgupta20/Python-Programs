# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 11:11:11 2019

@author: Saksham
"""

count=0
s1=list(input())
s2=list(input())
for i in set(s1):
    if i in s2:
        count+=2*(min(s1.count(i),s2.count(i)))
count=len(s1)+len(s2)-count
print(count)
    