# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 18:05:24 2019

@author: Saksham
"""


"""
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer e at position i.
print: Print the list.
remove e: Delete the first occurrence of integer e.
append e: Insert integer e at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types listed above. Iterate through each command in order and perform the corresponding operation on your list.
"""

list1=[]
N = int(input())
for i in range(N):
    x=input().split()
    cmd=x[0];
    args=x[1:]
    if cmd!="print":
        y=",".join(args)
        y="("+y+")"
        y=cmd+y
        eval("list1."+y)
    else:
        print(list1)

