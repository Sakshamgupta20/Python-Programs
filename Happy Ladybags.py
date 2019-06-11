# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 21:08:36 2019

@author: Saksham
"""

def happyLadybugs(b):
    if '_' in b:
        a=set(b)
        for i in a:
            if i!="_" and not b.count(i)>=2:
                return('NO')
        return("YES")
    else:
        a=set(b)
        for i in a:
            if not b.count(i)>=2:
                return('NO')
        for i in range(1,len(b)-1):
            if b[i-1]!=b[i] and b[i+1]!=b[i]:
                return("NO")
                return('NO')
        return("YES")
        
print(happyLadybugs('AABBC'))