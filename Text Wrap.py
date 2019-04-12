# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 20:26:46 2019

@author: Saksham
"""

"""
You are given a string S and width w. 
Your task is to wrap the string into a paragraph of width w.
"""
thickness = int(5) #This must be an odd number
c = 'H'

def wrap(string, max_width):
    x=''
    k=0
    c=0
    for j in range(max_width,len(string),max_width):
        s=string[k:j]
        k=k+max_width
        c=j
        x=x+s+"\n"
    if(len(string)>c):
        x=x+string[c-len(string):]+"\n"
    return(x)
wrap('ABCDEFGHIJKLIMNOQRSTUVWXYZ',4)

