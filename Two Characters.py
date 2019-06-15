# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 11:50:19 2019

@author: Saksham
"""

"""
In this challenge, you will be given a string. You must remove characters until the string is made up of any two alternating characters. When you choose a character to remove, all instances of that character must be removed. Your goal is to create the longest string possible that contains just two alternating letters.

As an example, consider the string abaacdabd. If you delete the character a, you will be left with the string bcdbd. Now, removing the character c leaves you with a valid string bdbd having a length of 4. Removing either b or d at any point would not result in a valid string.
"""
from itertools import combinations
def alternate(s):
    x=set(s)
    res=[]
    if len(x)<2:
        return 0
    else:
        combos=list(combinations(x,len(x)-2))
        print(combos)
        for i in combos:
            temp=s
            vals=[]
            for j in i:
                temp=temp.replace(j,"")
            for k in range(len(temp)-1):
                if temp[k]==temp[k+1]:
                    vals.append(False)
                else:
                    vals.append(True)
            print(temp)
            if all(vals):
                res.append(len(temp))
            else:
                res.append(0)
    return(max(res))
            
alternate('beabeefeab')
