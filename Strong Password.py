# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 11:03:51 2019

@author: Saksham
"""

"""
Louise joined a social networking site to stay in touch with her friends. The signup page required her to input a name and a password. However, the password must be strong. The website considers a password to be strong if it satisfies the following criteria:

Its length is at least 6.
It contains at least one digit.
It contains at least one lowercase English character.
It contains at least one uppercase English character.
It contains at least one special character. The special characters are: !@#$%^&*()-+
"""

import re
def minimumNumber(n, password):
    res=0
    upper=bool(re.search("[A-Z]",password))
    lower=bool(re.search("[a-z]",password))
    special=bool(re.search("[!@#$%^&*()+-]",password))
    digit=bool(re.search("[0-9]",password))
    for i in [upper,lower,special,digit]:
        if not i:
            res+=1
    return(max(res,6-n))
print(minimumNumber(7,'AUzs-nV'))