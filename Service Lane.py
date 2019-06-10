# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 10:37:22 2019

@author: Saksham
"""

def serviceLane(n, cases):
    print(n)
if __name__ == '__main__':
    nt = input().split()

    n = int(nt[0])

    t = int(nt[1])

    width = list(map(int, input().rstrip().split()))

    cases = []

    for _ in range(t):
        cases.append(list(map(int, input().rstrip().split())))

    result = serviceLane(width, cases)
    print(result)