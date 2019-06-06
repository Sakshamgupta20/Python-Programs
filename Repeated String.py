# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 11:07:11 2019

@author: Saksham
"""

"""
Lilah has a string, s, of lowercase English letters that she repeated infinitely many times.

Given an integer,n , find and print the number of letter a's in the first n letters of Lilah's infinite string.

For example, if the string s='abcac' and n=10, the substring we consider is abcacabcac, the first 10 characters of her infinite string. There are 4 occurrences of a in the substring.
"""

import math
def repeatedString(s, n):
    x=n%len(s)
    print(x)
    count=0
    if(x!=0):
        for i in range(x):
            if s[i]=='a':
                count+=1
    print(int((n-count)/len(s)))
    return int((s.count('a')* int((n-count)/len(s)))+count)
print(repeatedString('epsxyyflvrrrxzvnoenvpegvuonodjoxfwdmcvwctmekpsnamchznsoxaklzjgrqruyzavshfbmuhdwwmpbkwcuomqhiyvuztwvq',549382313570))
