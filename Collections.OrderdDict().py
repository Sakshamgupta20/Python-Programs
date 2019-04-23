# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 21:29:59 2019

@author: Saksham
"""


"""
You are the manager of a supermarket. 
You have a list of N items together with their prices that consumers bought on a particular day. 
Your task is to print each item_name and net_price in order of its first occurrence.
"""

from collections import OrderedDict

dict1=OrderedDict()
dict_count=OrderedDict()
n=int(input())
for i in range(n):
    x=list(input().split())
    dict1[' '.join(x[0:len(x)-1])]=int(x[-1])
    if not ' '.join(x[0:len(x)-1]) in dict_count:
        dict_count[' '.join(x[0:len(x)-1])]=1
    else:
        dict_count[' '.join(x[0:len(x)-1])]+=1

for product,value in dict1.items():
    print(product,dict_count[product]*value)
    
    



