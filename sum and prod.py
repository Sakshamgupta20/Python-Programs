# -*- coding: utf-8 -*-
"""
Created on Wed May 29 17:28:00 2019

@author: Saksham
"""

import numpy
n,m=map(int,input().split())
print(numpy.prod(numpy.sum([list(map(int,input().split())) for i in range(n)],axis=0)))