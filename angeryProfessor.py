# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 12:38:42 2019

@author: Saksham
"""




def angryProfessor(k, a):
    saver = 0
    for i in a:
        if(i <= 0):
            saver += 1
    print(saver)
    if(k > saver):
       return "YES"   
    return "NO"
    
    
    
    
print(angryProfessor(6,list(map(int,'-58 -29 -35 -18 43 -28 -76 43 -13 6'.split()))))