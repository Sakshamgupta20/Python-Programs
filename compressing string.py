# -*- coding: utf-8 -*-
"""
Created on Tue May 21 17:22:13 2019

@author: Saksham
"""

from collections import OrderedDict
x=OrderedDict()
for i in range(int(input())):
    a=input()
    if a not in x:
        x[a]=1
    else:
        x[a]+=1
print(len(x),print(*[j for i,j in x.items()]))