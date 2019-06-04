# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 21:48:35 2019

@author: Saksham
"""

"""
sticks-length         length-of-cut   sticks-cut
1 2 3 4 3 3 2 1         1               8
_ 1 2 3 2 2 1 _         1               6
_ _ 1 2 1 1 _ _         1               4
_ _ _ 1 _ _ _ _         1               1
_ _ _ _ _ _ _ _       DONE            DONE

"""

def cutTheSticks(arr):
    res=[]
    while(len(arr)!=0):
        res.append(len(arr))
        m=min(arr)
        arr=list(filter(lambda fu: fu-m, arr))
    return(res)
    
cutTheSticks([1,2,3,4,3,3,2,1])