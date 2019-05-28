# -*- coding: utf-8 -*-
"""
Created on Tue May 28 16:41:29 2019

@author: Saksham
"""
"""
searching floating point number
"""
import re
x=re.search("^[|+-]?\d*\.\d+$","-.555555555")
print(bool(x))