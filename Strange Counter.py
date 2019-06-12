# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 22:41:38 2019

@author: Saksham
"""

"""
Bob has a strange counter. At the first second, it displays the number 3. Each second, the number displayed by the counter decrements by 1 until it reaches 1.

The counter counts down in cycles. In next second, the timer resets to 2 * the initial number for the prior cycles and continues counting down.

Find and print the value displayed by the counter at time t.
"""

def strangeCounter(t):
    x=3
    y=3
    s=1
    while(y<t):
        x=x*2
        y+=x
        s=y-x+1
    return(x-(t-s))
print(strangeCounter(9))