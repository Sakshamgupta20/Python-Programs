# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 17:04:53 2019

@author: Saksham
"""



"""
Input ex

 16
 1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
 4
 intersection_update 10
 2 3 5 6 8 9 1 4 7 11
 update 2
 55 66
 symmetric_difference_update 5
 22 7 35 62 58
 difference_update 7
 11 22 35 55 58 62 66
"""
n=input()
numbers=set(input().split())
for i in range(int(input())):
    x=input()
    cmd,args=x.split()
    ex=set(input().split())
    x="numbers."+cmd+"(ex)"
    exec(x)
numbers=map(int,numbers)
print(sum(numbers))