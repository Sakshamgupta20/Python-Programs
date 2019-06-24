# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 11:19:23 2019

@author: Saksham
"""

s=list(input())
res=[]
flag=1
for i in set(s):
    if s.count(i)%2!=0:
        res.append(i)
    if(len(res)>1):
        flag=0
        break
if(flag==0):
    print('NO')
else:
    print('YES')