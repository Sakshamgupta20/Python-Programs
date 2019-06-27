# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 18:24:55 2019

@author: Saksham
"""
def morganAndString(a, b):
    answer = ''
    a += '~'
    b += '~'
    i = 0
    j = 0
    while a[i] != '~' or b[j] != '~':
        if a[i] != '~' and a[i:] < b[j:]:
            answer += a[i]
            i += 1
        else:
            answer += b[j]
            j += 1
    return answer
for i in range(int(input())):
    s1=input()
    s2=input()
    print(morganAndString(s1,s2))