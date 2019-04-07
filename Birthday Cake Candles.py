# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 21:43:12 2019

@author: Saksham
"""

"""
You are in charge of the cake for your niece's birthday and have decided the cake will have one candle for each year of her total age. When she blows out the candles, she’ll only be able to blow out the tallest ones. Your task is to find out how many candles she can successfully blow out.

For example, if your niece is turning 4 years old, and the cake will have 4 candles of height 4,4 ,1 ,3 , she will be able to blow out 2 candles successfully, since the tallest candles are of height 4 and there are 2 such candles.
"""

def birthdayCakeCandles(ar):
    ar.sort()
        count=1
        for i in range(0,len(ar)-1):
            if ar[len(ar)-1]==ar[i]: count=count+1
            return count