# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 18:27:49 2019

@author: Saksham
"""
for i in range(int(input())):
    try:
        a,b=input().split()
        print(int(int(a)//int(b)))
    except ZeroDivisionError as e:
        print("Error Code:",e)
    except ValueError as e:
        print("Error Code:",e)
