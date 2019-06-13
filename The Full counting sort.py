# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 17:57:42 2019

@author: Saksham
"""

"""
In this challenge you need to print the string that accompanies each integer in a list sorted by the integers. If two strings are associated with the same integer, they must be printed in their original order so your sorting algorithm should be stable. There is one other twist. The first half of the strings encountered in the inputs are to be replaced with the character "-".

Insertion Sort and the simple version of Quicksort are stable, but the faster in-place version of Quicksort is not since it scrambles around elements while sorting.

In this challenge, you will use counting sort to sort a list while keeping the order of the strings preserved.


20
0 ab
6 cd
0 ef
6 gh
4 ij
0 ab
6 cd
0 ef
6 gh
0 ij
4 that
3 be
0 to
1 be
5 question
1 or
2 not
4 is
2 to
4 the

- - - - - to be or not to be - that is the question - - - -
"""
n=int(input())

a=[[] for i in range(100)]
for i in range(n):
    x,s=input().split()
    if i < n//2:
        s="-"
    a[int(x)].append(s)


print(*[element for sublist in a for element in sublist])
            
            

            
            
            
            
            
            
            
