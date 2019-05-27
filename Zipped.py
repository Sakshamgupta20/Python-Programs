# -*- coding: utf-8 -*-
"""
Created on Mon May 27 12:16:08 2019

@author: Saksham
"""

"""
1 line solution to find AVERAGE SCORES

Student ID → ___1_____2_____3_____4_____5__               
Subject 1   |  89    90    78    93    80
Subject 2   |  90    91    85    88    86  
Subject 3   |  91    92    83    89    90.5
            |______________________________
Average        90    91    82    90    85.5 

"""


N,X=map(int,input().split())
print(*[sum(j)/X for j in zip(*[list(map(float,input().split())) for i in range(X)])],sep='\n')
