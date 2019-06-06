# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 12:05:11 2019

@author: Saksham
"""

def equalizeArray(arr):
    max1=0
    for i in set(arr):
        if arr.count(i)>max1:
            max1=arr.count(i)
    return(len(arr)-max1)
    
    
equalizeArray([1,2,2,3])