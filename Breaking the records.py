# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 19:50:27 2019

@author: Saksham
"""

"""
Maria plays college basketball and wants to go pro. Each season she maintains a record of her play. She tabulates the number of times she breaks her season record for most points and least points in a game. Points scored in the first game establish her record for the season, and she begins counting from there.
"""

def breakingRecords(scores):
    highest=scores[0]
    lowest=scores[0]
    l,h=0,0
    for i in range(1,len(scores)):
        if scores[i]>highest:
            highest=scores[i]
            h+=1
        elif scores[i]<lowest:
            lowest=scores[i]
            l+=1
    res=h,l
    return res
scores=[3,4,21,36,10,28,35,5,24,42]
breakingRecords(scores)