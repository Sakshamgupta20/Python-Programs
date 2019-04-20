# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 22:24:06 2019

@author: Saksham
"""

n=int(input())
n1=input().split().index("MARKS")
sum=0
for i in range(n):sum=sum+int(input().split()[n1])
print(sum/n)