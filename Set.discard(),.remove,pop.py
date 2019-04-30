# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 15:41:02 2019

@author: Saksham
"""


n=input()
numbers=set(map(int,input().split()))
for i in range(int(input())):
    x=input()
    if x!='pop':
        cmd,args=x.split()
        x="numbers."+cmd+"("+args+")"
    else:
        x="numbers."+x+"()"
    exec(x)
print(sum(numbers))