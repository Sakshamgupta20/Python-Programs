# -*- coding: utf-8 -*-
"""
Created on Fri May 31 11:21:51 2019

@author: Saksham
"""


def pageCount(n, p):
    max=0
    if(p<=n/2):    
        for i in range(0,n+1,2):
            if(i==p or i+1==p):
                break;
            else:
                max+=1
    else:
        if n%2!=0:
            for i in range(n,-1,-2):
                if(i==p or i-1==p):
                    break;
                else:
                    max+=1
        else:
            for i in range(n+1,-1,-2):
                if(i==p or i-1==p):
                    break;
                else:
                    max+=1
    print(max)
    
pageCount(6,5)