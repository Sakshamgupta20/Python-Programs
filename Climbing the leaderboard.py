# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 12:32:27 2019

@author: Saksham
"""

"""
Alice is playing an arcade game and wants to climb to the top of the leaderboard and wants to track her ranking. The game uses Dense Ranking, so its leaderboard works like this:

The player with the highest score is ranked number 1 on the leaderboard.
Players who have equal scores receive the same ranking number, and the next player(s) receive the immediately following ranking number.
For example, the four players on the leaderboard have high scores of 70, 80, 105, and 80. Those players will have ranks 1, 2, 2, and ,3 respectively. If Alice's scores are 70,80  and 105, her rankings after each game are 4th,3rd  and 1st.
"""

from bisect import *
n = int(input())
scores = list(set(map(int, input().split())))
l = len(scores)
scores.sort()
m = int(input())
alice = map(int, input().split())
for i in alice:
    print (l - bisect_right(scores, i) + 1)