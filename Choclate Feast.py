# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 10:12:09 2019

@author: Saksham
"""

"""
Little Bobby loves chocolate. He frequently goes to his favorite 5 & 10 store, Penny Auntie, to buy them. They are having a promotion at Penny Auntie. If Bobby saves enough wrappers, he can turn them in for a free chocolate.

For example, Bobby has n=15 to spend on bars of chocolate that cost c=3 each. He can turn in m=2 wrappers to receive another bar. Initially, he buys 5 bars and has 5 wrappers after eating them. He turns in 4 of them, leaving him with 1, for 2 more bars. After eating those two, he has 3 wrappers, turns in 2 leaving him with 1 wrapper and his new bar. Once he eats that one, he has 2 wrappers and turns them in for another bar. After eating that one, he only has 1 wrapper, and his feast ends. Overall, he has eaten  5+2+1+1=9 bars.
"""

def chocolateFeast(n, c, m):
    chocates=int(n/c)
    chc=[chocates]
    while(chocates>=m):
        chc.append(int(chocates/m))
        chocates=(chocates-int(chocates/m)*m)+int(chocates/m)
        print(chocates)
    return(sum(chc))
print(chocolateFeast(6,2,2))








