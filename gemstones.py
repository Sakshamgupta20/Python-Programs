# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 14:21:44 2019

@author: Saksham
"""

"""
John has collected various rocks. Each rock has various minerals embeded in it. Each type of mineral is designated by a lowercase letter in the range ascii[a-z]. There may be multiple occurrences of a mineral in a rock. A mineral is called a gemstone if it occurs at least once in each of the rocks in John's collection.

Given a list of minerals embedded in each of John's rocks, display the number of types of gemstones he has in his collection.

For example, the array of mineral composition strings arr=[abc,abc,bc]. The minerals b and c appear in each composite, so there are 2 gemstones.
"""

arr=[]
count=0
for i in range(int(input())):
    arr.append(input())
for i in set(arr[0]):
    x=[-1 for j in arr if i not in j]
    if len(x)==0:
        count+=1
print(count)       