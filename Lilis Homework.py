# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 12:32:11 2019

@author: Saksham
"""

"""
 An array is beautiful if the sum of arr[i]-arr[i-1] among 0<i<n among  is minimal.
Given the array arr, determine and return the minimum number of swaps that should be performed in order to make the array beautiful.
"""
def homework(n, arr):
    pos=dict()
    for i,num in enumerate(arr):
        pos[num]=i
    count=0
    x=sorted(arr)
    
    for i in range(len(arr)):
        if arr[i]!=x[i]:
            count+=1
            
            new_idx=pos[x[i]]
            pos[arr[i]]=new_idx
            arr[i],arr[new_idx]=arr[new_idx],arr[i]
    return(count)


n=int(input())
x=list(map(int,input().split()))
asc=homework(n,list(x))
desc=homework(n,list(reversed(x)))
print(min(asc,desc))