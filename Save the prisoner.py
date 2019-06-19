# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 18:19:27 2019

@author: Saksham
"""
"""
A jail has a number of prisoners and a number of treats to pass out to them. Their jailer decides the fairest way to divide the treats is to seat the prisoners around a circular table in sequentially numbered chairs. A chair number will be drawn from a hat. Beginning with the prisoner in that chair, one candy will be handed to each prisoner sequentially around the table until all have been distributed.

The jailer is playing a little joke, though. The last piece of candy looks like all the others, but it tastes awful. Determine the chair number occupied by the prisoner who will receive that candy.
"""
for i in range(int(input())):
    n,m,d=input().split()
    n,m,d=int(n),int(m),int(d)
    if((m+d-1)%n==0):
        print(n)
    else:
        print((m+d-1)%n)