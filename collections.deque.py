# -*- coding: utf-8 -*-
"""
Created on Tue May 21 18:49:29 2019

@author: Saksham
"""

from collections import deque
x=deque()
for i in range(int(input())):
    a=input().split()
    if len(a)==1:
        a="x."+a[0]+"()"
        exec(a)
    else:
        a="x."+a[0]+"("+a[1]+")"
        exec(a)
print(*[item for item in x])
