# -*- coding: utf-8 -*-
"""
Created on Thu May 30 13:42:32 2019

@author: Saksham
"""

"""
Determining Socks pairs
"""


def sockMerchant(n, ar):
    a=dict()
    for i in ar:
        if i not in a:
            a[i]=1
        else:
            a[i]+=1
    count=0
    print(a)
    for k,v in a.items():
        if v%2!=0:
            count+=(v-1)/2
        else:
            count+=v/2
    return(count)
print(sockMerchant(6,[10,20,20,10,10,30,50,10,20]))