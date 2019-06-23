# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 23:50:57 2019

@author: Saksham
"""

n=int(input())
for i in range(n):
    s=list(input())
    if list(reversed(s))==s:
        print(-1)
    else:
        for j in range(1,(len(s)//2)+1):
            if s[j-1]!=s[-j]:
                break
        s1=s[:]
        del s[j-1]
        del s1[-j]
        if (list(reversed(s))==s):
            print(j-1)
        else:
            print(len(s)+1-j)