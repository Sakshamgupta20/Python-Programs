# -*- coding: utf-8 -*-
"""
Created on Wed May 22 18:18:01 2019

@author: Saksham
"""


"""
Print the three most common characters along with their occurrence count each on a separate line. 
Sort output in descending order of occurrence count. 
If the occurrence count is the same, sort the characters in alphabetical order.
"""

a='aabbbccde'

from collections import OrderedDict
a=list(a)
b=OrderedDict()
for i in a:
    if a.count(i) not in b:
        b[a.count(i)]=[i]
    else:
        b[a.count(i)].append(i)
sorted_dictionary = OrderedDict(sorted(b.items(), key=lambda v: v, reverse=True))
count=0
for i,j in sorted_dictionary.items():
    j=set(j)
    j=sorted(j)
    for k in j:
        print(k ,i)
        count=count+1
        if count==3:
            break
    if count==3:
        break