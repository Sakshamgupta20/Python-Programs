# -*- coding: utf-8 -*-
"""
Created on Fri May 31 15:41:42 2019

@author: Saksham
"""

"""
picking numbers which have difference of 1
"""
from itertools import combinations
def pickingNumbers(a):
    y=a
    if len(set(a))==1:
        return(len(a))
    else:
        x=combinations(set(a),2)
        count=0
        for i in set(a):
            if a.count(i)>count:
                count=a.count(i)
        for i in x:
            if(abs(i[1]-i[0])<=1):
                if a.count(i[1])+a.count(i[0])>count:
                    count=a.count(i[1])+a.count(i[0])
        return(count)
        
lis='4 97 5 97 97 4 97 4 97 97 97 97 4 4 5 5 97 5 97 99 4 97 5 97 97 97 5 5 97 4 5 97 97 5 97 4 97 5 4 4 97 5 5 5 4 97 97 4 97 5 4 4 97 97 97 5 5 97 4 97 97 5 4 97 97 4 97 97 97 5 4 4 97 4 4 97 5 97 97 97 97 4 97 5 97 5 4 97 4 5 97 97 5 97 5 97 5 97 97 97'.split(" ")
lis=list(map(int,lis))
print(pickingNumbers(lis))