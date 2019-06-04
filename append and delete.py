# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 17:29:51 2019

@author: Saksham
"""


"""
Complete the appendAndDelete function in the editor below. It should return a string, either Yes or No.

appendAndDelete has the following parameter(s):

s: the initial string
t: the desired string
k: an integer that represents the number of operations

"""

def appendAndDelete(s, t, k):
    r=min(len(s),len(t))
    count=0
    for i in range(r):
        if s[i]==t[i]:
            count+=1
        else:
            break
    if(s==t):
        return("Yes")
    else:
        if (k-(len(s)-count))-(len(t)-count)==0:
            return("Yes")
        else:
            if(count==len(s)):
                for i in range(count):
                    if(k-(len(t)-count)-i)==0:
                        return("Yes")
                return("No")
            if(k-len(s)-len(t)>=0):
                return("Yes")
            for i in range(count):
                if(k-i-len(t))==0:
                    return("Yes")
            return("No")
    
print(appendAndDelete('aaa','a',5))