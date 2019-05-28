# -*- coding: utf-8 -*-
"""
Created on Tue May 28 17:25:02 2019

@author: Saksham
"""

def fibonacci(n):
    i=0
    j=1
    x=[]
    if n==0:
        x=[]
    elif n==1:
        x.append(i)
    else:
        x.append(i)
        x.append(j)
        while(len(x)!=n):
            x.append(i+j)
            t=i+j
            i=j
            j=t
    return(x)

if __name__ == '__main__':
    n = int(input())
    print(list(map(lambda x: x*x*x, fibonacci(n))))
    