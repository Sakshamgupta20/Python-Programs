# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 20:40:24 2019

@author: Saksham
"""

n=int(input())
x=list(map(int,input().split()))
x1=sorted(x)
res=[]
for i in range(n):
    if(x[i]!=x1[i]):
        res.append(i)
if len(res)==0:
    print('no')
elif len(res)==1:
    print('no')
elif len(res)==2:
    if(x[res[0]]==x1[res[1]] and x[res[1]]==x1[res[0]]):
        print('yes')
        print('swap',res[0]+1,res[1]+1)
else:
    for k in range(len(res)):
        if(x[res[k]]!=x1[res[len(res)-k-1]]):
            print('no')
            break
    else:
        print('yes')
        print('reverse',res[0]+1,res[-1]+1)
            
        
        