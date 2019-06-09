# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 23:03:12 2019

@author: Saksham
"""

def timeInWords(h, m):
    x=["zero","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty","twenty one","twenty two","twenty three","twenty four","twenty five","twenty six","twenty seven","twenty eight","twenty nine","thirty","thirty one","thirty two","thirty three","thirty four","thirty five","thirty six","thirty seven","thirty eight","thirty nine","forty","forty one","forty two","forty three","forty four","forty five","forty six","forty seven","forty eight","forty nine","fifty","fifty one","fifty two","fifty three","fifty four","fifty five","fifty six","fifty seven","fifty eight","fifty nine","sixty"]
    if(m==00):
        return(x[h] + " o' clock")
    elif(m<=30):
        if m==1:
            return ("one minute past "+x[h])
        if m==15:
            return ("quarter past "+x[h])
        if m==30:
            return ("half past "+x[h])
        else:
            return (x[m] + " minutes past " + x[h])
    elif(m>30):
        if m==45:
            return ("quarter to "+x[h+1])
        elif m==59:
            return ("one minute to "+x[h+1])
        else:
            return (x[60-m] + " minutes to " + x[h+1])
print(timeInWords(5,47))