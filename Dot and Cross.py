# -*- coding: utf-8 -*-
"""
Created on Wed May 29 17:57:05 2019

@author: Saksham
"""

import numpy
numpy.set_printoptions(legacy='1.13')
n=int(input())
x=[list(map(int,input().split())) for i in range(n)]
y=[list(map(int,input().split())) for i in range(n)]
print(numpy.dot(x,y))