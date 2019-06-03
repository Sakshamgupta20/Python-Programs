# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 12:40:13 2019

@author: Saksham
"""

def permutationEquation(p):
    res=[]
    for i in range(1,len(p)+1):
        index=p.index(i)+1
        index=p.index(index)+1
        res.append(index)
    return(res)
            
        
print(permutationEquation([4,3,5,1,2]))