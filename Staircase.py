# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 19:03:26 2019

@author: Saksham
"""
"""
Observe that its base and height are both equal to , and the image is drawn using # symbols and spaces. The last line is not preceded by any spaces.
Write a program that prints a staircase of size .
eg: if n=4
   #
  ##
 ###
####
"""
def staircase(n):
    for i in range(n):
        for j in range(n-1):
            print(end=" ")
        n=n-1
        for j in range(i+1):
            print("#",end="")
        print("\r")

staircase(4)