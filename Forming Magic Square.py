# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 11:26:30 2019

@author: Saksham
"""


pre = [
            [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
            [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
            [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
            [[2, 9, 4], [7, 5, 3], [6, 1, 8]], 
            [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
            [[4, 3, 8], [9, 5, 1], [2, 7, 6]], 
            [[6, 7, 2], [1, 5, 9], [8, 3, 4]], 
            [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
            ]
s = []
total1=[]
for _ in range(3):
    s.append(list(map(int, input().rstrip().split())))
for i in pre:
    total=0
    for prow,srow in zip(i,s):
        for j,k in zip(prow,srow):
            if i!=j:
                total+=abs(j-k)
    total1.append(total)
print(min(total1))
