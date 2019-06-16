# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 13:15:11 2019

@author: Saksham
"""

def seperateNumbers(s):
    if s[0]==s:
        print('NO')
    for i in range(1,len(s)):
        mys=[]
        mys.append(s[:i])
        while len(''.join(mys))<len(s):
            mys.append(str(int(mys[-1])+1))
        if ''.join(mys)==s:
            print('YES',mys[0])
            break
        if i==len(s)-1:
            print('NO')
            
for i in range(int(input())):
    seperateNumbers(input().strip())