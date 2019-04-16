# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 18:54:11 2019

@author: Saksham
"""

"""
Raghu is a shoe shop owner. His shop has X number of shoes. 
He has a list containing the size of each shoe he has in his shop. 
There are N number of customers who are willing to pay xi amount of money only if they get the shoe of their desired size.

Your task is to compute how much money Raghu earned.
"""

from collections import Counter
n1=input()
shoes=Counter(list(map(int,input().split())))
n2=input()
x=[]
for i in range(int(n2)): x.append(list(map(int,input().split())))
income=0
for size,price in x:
    if shoes[size]:
        income+=price
        shoes[size]-=1
print(income)