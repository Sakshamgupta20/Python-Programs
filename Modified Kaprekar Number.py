# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 11:36:11 2019

@author: Saksham
"""

def kaprekarNumbers(p, q):
    result=[]
    for i in range(p,q+1):
        if i in [0,1]:
            result.append(i)
        else:
            if i in [2,3]:
                continue
            else:
                a=""
                num=str(i*i)
                for j in range(0,int(len(num)/2)):
                    a+=num[j]
                first=int(a)
                a=''
                for j in range(int(len(num)/2),len(num)):
                    a+=num[j]
                second=int(a)
            if(first+second==i):
                result.append(i)
    if(result):
        print(*result)
    else:
        print("INVALID RANGE")
kaprekarNumbers(400,700)