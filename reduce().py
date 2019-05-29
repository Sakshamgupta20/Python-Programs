# -*- coding: utf-8 -*-
"""
Created on Wed May 29 12:44:10 2019

@author: Saksham
"""

from fractions import Fraction
from functools import reduce

def product(fracs):
    x=Fraction(reduce(lambda x, y : x *y,fracs))
    return(x.numerator,x.denominator)

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)