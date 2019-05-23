# -*- coding: utf-8 -*-
"""
Created on Thu May 23 14:43:30 2019

@author: Saksham
"""

"""
You are given a space separated list of integers. If all the integers are positive, then you need to check if any integer is a palindromic integer.
"""
n,x=input(),list(map(str,input().split()))
print(all([int(i)>0 for i in x]) and any([j == j[::-1] for j in x]))
    