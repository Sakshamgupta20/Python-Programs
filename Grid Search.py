# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 13:28:26 2019

@author: Saksham
"""

"""
Given a 2D array of digits or grid, try to find the occurrence of a given 2D pattern of digits. For example, consider the following grid:

1234567890  
0987654321  
1111111111  
1111111111  
2222222222  
Assume we need to look for the following 2D pattern array:

876543  
111111  
111111
The 2D pattern begins at the second row and the third column of the grid. The pattern is said to be present in the grid.

"""
import re
def gridSearch(G, P):
    res=[]
    for i in range(len(G)):
        x=bool(re.search(P[0],G[i]))
        if(x):
            res.append(i)
    if(res):
        for i in res:
            res1=[]
            y=list(re.finditer(P[0],G[i]))
            for k1 in y:
                ii=i
                for j in range(1,len(P)):
                    ii=ii+1
                    if(i<len(G)):
                        x=re.finditer(P[j],G[ii])
                        if(x):
                            for k in list(x):
                                if(k1.start()==k.start() and k1.end()==k.end()):
                                    res1.append(1)
                                    break
                if(len(res1)+1==len(P)):
                    return('YES')
    else:
        return('NO')
    return('NO')
    
print(gridSearch("""999999
121211""".split("\n"),
"""99
11""".split("\n")))

