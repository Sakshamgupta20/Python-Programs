# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 22:21:44 2019

@author: Saksham
"""

"""
Calculate and print the sum of the elements in an array, keeping in mind that some of those integers may be quite large.
"""

def aVeryBigSum(ar):
    sum=0
    for i in ar:
        sum=sum+i
    return sum