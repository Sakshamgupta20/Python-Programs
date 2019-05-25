# -*- coding: utf-8 -*-
"""
Created on Sat May 25 11:24:44 2019

@author: Saksham
"""

"""
For every string listed, print "YES" if it is a valid mobile number and "NO" if it is not on separate lines. Do not print the quotes.
A valid mobile number is a ten digit number starting with a  7,8 or 9
"""

import re
for i in range(int(input())):
    if(re.search('^([7-9]\d{9})$',input())):
        print('YES')
    else:
        print("NO")
