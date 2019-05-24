# -*- coding: utf-8 -*-
"""
Created on Fri May 24 13:32:37 2019

@author: Saksham
"""

"""
Output a single line consisting of the probability that at least one of the K indices selected contains the letter:''.
"""
import itertools
n,x,r=input(),input().split(),input()
x=list(itertools.combinations(x,int(r)))
l=filter(lambda x2: 'a' in x2, x)
print('%.3f'%(len(list(l))/len(x)))

