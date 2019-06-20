# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 11:42:21 2019

@author: Saksham
"""

"""
Complete the beautifulTriplets function in the editor below. It must return an integer that represents the number of beautiful triplets in the sequence.

beautifulTriplets has the following parameters:

d: an integer
arr: an array of integers, sorted ascending

Recall that a beautiful triplet satisfies the following equivalence relation:arr[j]-arr[i]=arr[k]-arr[j]=d where 
"""
n,d=input().split()
d=int(d)
count=0
numbers=list(map(int,input().split()))
for i in numbers:
    if(i+d in numbers and i+2*d in numbers):
        count+=1
print(count)
