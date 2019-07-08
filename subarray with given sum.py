# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 11:26:29 2019

@author: Saksham
"""

"""
Given an unsorted array A of size N of non-negative integers, find a continuous sub-array which adds to a given number S.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of two lines. The first line of each test case is N and S, where N is the size of array and S is the sum. The second line of each test case contains N space separated integers denoting the array elements.

Output:
For each testcase, in a new line, print the starting and ending positions(1 indexing) of first such occuring subarray from the left if sum equals to subarray, else print -1.
"""

for i in range(int(input())):
    n,s=map(int,input().split())
    x=list(map(int,input().split()))
    header=0
    wsum=0
    flag=0
    for j in range(n):
        wsum+=x[j]
        while(wsum>s):
            wsum-=x[header]
            header+=1
        if(wsum==s):
            flag=1
            break
    if(flag==0):
        print('-1')
    else:
        print(header+1,j+1)
        
        