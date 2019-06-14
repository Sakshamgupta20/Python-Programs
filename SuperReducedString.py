# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 15:32:49 2019

@author: Saksham
"""

def superReducedString(s):
    x=[]
    for i in s:
        if(x):
            if(x[-1]==i):
                x.pop()
            else:
                x.append(i)
        else:
            x.append(i)
    if(x):
        return(''.join(x))
    else:
        return("Empty String")
print(superReducedString('aaaabbccdddd'))
    
        
