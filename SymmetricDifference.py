# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 22:25:33 2019

@author: Saksham
"""

a,b = [set(input().split()) for _ in range(4)][1::2]
print ('\n'.join(sorted(a^b, key=int)))