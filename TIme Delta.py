# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 20:29:46 2019

@author: Saksham
"""

"""
Time Difference
"""
from datetime import datetime as dt

fmt = '%a %d %b %Y %H:%M:%S %z'
for i in range(int(input())):
    print(int(abs((dt.strptime(input(), fmt) - 
                   dt.strptime(input(), fmt)).total_seconds())))

