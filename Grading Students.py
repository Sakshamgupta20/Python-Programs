# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 19:03:26 2019

@author: Saksham
"""


"""
HackerLand University has the following grading policy:

Every student receives a grade in the inclusive range from 0 to 100 .
Any grade less than 40 is a failing grade.
Sam is a professor at the university and likes to round each student's grade according to these rules:

If the difference between the grade and the next multiple of 5 is less than 3, round grade up to the next multiple of 5 .
If the value of grade is less than , no rounding occurs as the result will still be a failing grade.
For example, grade=84  will be rounded to 85 but grade=29 will not be rounded because the rounding would result in a number that is less than 40.

Given the initial value of grade for each of Sam's  n students, write code to automate the rounding process.

eg. Input=73,67,38,33
Output=75,67,40,33
"""
arr=[73,67,38,33]
nj=0
final=list()
for i in arr:
    if i>=38: 
        for j in range(i):
            nj=5*j
            if i<5*j:
                if(nj-i<3):
                    final.append(nj)
                    break
                else:
                    final.append(i)
                    break
    else:
        final.append(i)
