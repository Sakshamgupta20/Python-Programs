# -*- coding: utf-8 -*-
"""
Created on Fri May 24 17:57:25 2019

@author: Saksham
"""
from itertools import product
n,M=map(int,input().split())
numbers= [list(map(int,input().split()))[1:] for i in range(n)]
results=map(lambda x: sum(i*i for i in x)%M , product(*numbers))
print(max(results))