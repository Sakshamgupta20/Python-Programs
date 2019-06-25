# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 11:34:44 2019

@author: Saksham
"""
"""
Sherlock considers a string to be valid if all characters of the string appear the same number of times. It is also valid if he can remove just 1 character at 1 index in the string, and the remaining characters will occur the same number of times. Given a string s, determine if it is valid. If so, return YES, otherwise return NO.

"""
s=list(input())
res=[]
flag=1
for i in set(s):
    res.append(s.count(i))
    if(len(set(res))>2):
        flag=0
        print('NO')
        break
if(flag==1):
    if(len(set(res))==1):
        print('YES')
    else:
        flag1=0
        res1=list(set(res))
        for i in range(2):
            if(i==0):
                if(res.count(res1[0])==len(res)-1 and res1[i+1]-1==res[i+1]):
                    flag1=1
                    break
            elif(i==1):
                if(res.count(res1[1])==len(res)-1 and res1[i-1]==1):
                    flag1=1
        if(flag1==0):
            print('NO')
        else:
            print('YES')