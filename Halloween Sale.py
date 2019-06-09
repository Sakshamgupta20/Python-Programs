# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 22:33:24 2019

@author: Saksham
"""

def howManyGames(p, d, m, s):
    result=[p]
    while(sum(result)<s):
        if(result[-1]-d>m):
            result.append(result[-1]-d)
        else:
            result.append(m)
    res=len(result)
    if(sum(result)>s):
        res=res-1
    return(res)
print(howManyGames(16 ,2 ,1, 9981))