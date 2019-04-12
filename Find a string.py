# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 19:21:22 2019

@author: Saksham
"""

"""
In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.
"""
def count_substring(string, sub_string):
    count=0
    n=len(sub_string)
    for i in range(0,len(string)):
        y=''
        for j in range(n):
            ni=i+j
            if(ni<len(string)):
                y=y+string[ni]
        if(sub_string==y):
            count+=1
    return count
y=count_substring("ThIsisCoNfUsInG","is")