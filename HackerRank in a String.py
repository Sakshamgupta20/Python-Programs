# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 21:06:59 2019

@author: Saksham
"""


def hackerrankInString(s):
    p=0
    for i in 'hackerrank':
        if i in s[p:]:
            p=s.index(i,p)+1
            print(p)
        else:
            return('NO')
    return('YES')

print(hackerrankInString('rhbaasdndfsdskgbfefdbrsdfhuyatrjtcrtyytktjjt'))