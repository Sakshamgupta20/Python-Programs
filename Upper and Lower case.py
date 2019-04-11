# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 19:34:10 2019

@author: Saksham
"""

def swap_case(s):
    x=''
    for i in s:
        if i.isupper():
            i=i.lower()
        else:
            i=i.upper()
        x=x+i
    return x
y=swap_case("sAkS")