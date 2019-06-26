# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 11:56:25 2019

@author: Saksham
"""

"""
Two words are anagrams of one another if their letters can be rearranged to form the other word.

In this challenge, you will be given a string. You must split it into two contiguous substrings, then determine the minimum number of characters to change to make the two substrings into anagrams of one another.

For example, given the string 'abccde', you would break it into two parts: 'abc' and 'cde'. Note that all letters have been used, the substrings are contiguous and their lengths are equal. Now you can change 'a' and 'b' in the first substring to 'd' and 'e' to have 'dec' and 'cde' which are anagrams. Two changes were necessary.

Complete the anagram function in the editor below. It should return the minimum number of characters to change to make the words anagrams, or -1 if it's not possible.

anagram has the following parameter(s):

s: a string

"""


for i in range(int(input())):
    s=list(input())
    if(len(s)%2!=0):
        print(-1)
    else:
        s1=s[:len(s)//2]
        s2=s[len(s)//2:]
        x1,x2=[],[]
        temp=set(s1)
        temp.update(s2)
        for i in temp:
            if(i in s1):
                x1.append(s1.count(i))
            else:
                x1.append(0)
            if(i in s2):
                x2.append(s2.count(i))
            else:
                x2.append(0)
        print(sum([abs(x-y) for x,y in zip(x1,x2)])//2)
        