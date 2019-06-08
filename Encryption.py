# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 10:05:29 2019

@author: Saksham
"""


import math
def encryption(s):
    s=''.join(s.split(" "))
    result=[]
    result1=[]
    row=math.floor(math.sqrt(len(s)))
    column=math.ceil(math.sqrt(len(s)))
    a=''
    if not row*column >= len(s):
         if(row>=column):
            column+=1
         else:
            row+=1
    for i in s:
        a=a+i
        if(len(a)==column):
            result.append(a)
            a=''
    if(len(a)>0):
        result.append(a)
        a=''
    count=0
    for j in range(column):
        for i in result:
            if(len(i)>=count+1):
                a=a+i[count]
        result1.append(a)
        a=''
        count+=1
    return(" ".join(result1))
print(encryption('chillout'))