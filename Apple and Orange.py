# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 19:26:44 2019

@author: Saksham
"""

"""
Sam's house has an apple tree and an orange tree that yield an abundance of fruit.The red region denotes his house, where s is the start point, and t is the endpoint. The apple 
tree is to the left of his house, and the orange tree is to its right. You can assume the trees are located on a single point, where the apple tree is at point a, and the orange tree is at point b .

When a fruit falls from its tree, it lands d units of distance from its tree of origin along the x-axis. A negative value of d means the fruit fell d units to the tree's left, and a positive value of d means it falls d units to the tree's right.

Given the value of d for m apples and n oranges, determine how many apples and oranges will fall on Sam's house (i.e., in the inclusive range [s,t] )?
"""

def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples1=[]
    oranges1=[]
    for i in apples:
        i=i+a
        if i>=s and i<=t:
            apples1.append(i)
    for i in oranges:
        i=i+b
        if i>=s and i<=t:
            oranges1.append(i)
    print(len(apples1))
    print(len(oranges1))
    
    
apples=[-2,2,1]
oranges=[5,-6]
countApplesAndOranges(7,11,5,15,apples,oranges)