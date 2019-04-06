# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 23:36:53 2019

@author: Saksham
"""


"""

Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
"""

def timeConversion(s):
    s=list(s)
    if s[8]=="P":
        a=s[0]+(s[1])
        if(a!="12"):
            a=int(a)
            a=a+12
            a=str(a)
            s[0]=a[0]
            s[1]=a[1]
        s.remove("P")
        s.remove("M")
        s=''.join(s)
    else:
        a=s[0]+(s[1])
        if(a=="12"):
            s[0]="0"
            s[1]="0"
        s.remove("A")
        s.remove("M")
        s=''.join(s)
    return(s)
    
time1=timeConversion("07:05:45PM")