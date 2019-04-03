# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 19:03:26 2019

@author: Saksham
"""


"""
Given a square matrix, calculate the absolute difference between the sums of its diagonals.

"""
def diagonalDifference(arr):
    lend=len(arr)
    sum=0
    sum1=0
    count=0
    count1=lend-1
    for j in arr:
        sum1=sum1+j[count1]
        sum=sum+j[count]
        count=count+1
        count1=count1-1
        continue
    sum=sum-sum1
    if sum<0:
        sum=sum*-1
    return(sum)
    
arr=[[1,2,3],[4,5,6],[7,8,20]]
result=diagonalDifference(arr)
print(result)