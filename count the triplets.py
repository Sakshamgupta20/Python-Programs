# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 19:19:37 2019

@author: Saksham
"""

"""
Given an array of distinct integers. The task is to count all the triplets such that sum of two elements equals the third element.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of two lines. First line of each test case contains an Integer N denoting size of array and the second line contains N space separated elements.

Output:
For each test case, print the count of all triplets, in new line. If no such triplets can form, print "-1".
"""
for _ in range(int(input())):
    n=int(input())
    res=0
    x=list(map(int,input().split()))
    x_set=set(x)
    x.sort()
    for i in range(n):
        for j in range(i+1,n):
            s=x[i]+x[j]
            if(s>x[-1]):
                break
            if s in x_set:
                res+=1
    if(res==0):
        print(-1)
    else:
        print(res)