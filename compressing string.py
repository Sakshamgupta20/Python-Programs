# -*- coding: utf-8 -*-
"""
Created on Tue May 21 17:22:13 2019

@author: Saksham
"""

from itertools import groupby

x='1222311'

print(*[(len(list(j)),int(i)) for i,j in groupby(input())])