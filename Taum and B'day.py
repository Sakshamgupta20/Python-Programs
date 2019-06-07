# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 19:54:50 2019

@author: Saksham
"""


"""
Taum is planning to celebrate the birthday of his friend, Diksha. There are two types of gifts that Diksha wants from Taum: one is black and the other is white. To make her happy, Taum has to buy  black gifts and  white gifts.

The cost of each black gift is bc units.
The cost of every white gift is wc units.
The cost of converting each black gift into white gift or vice versa is z units.
Help Taum by deducing the minimum amount he needs to spend on Diksha's gifts.

"""
def taumBday(b, w, bc, wc, z):
    if(bc==wc):
        return(b*bc+w*wc)
    elif(bc<wc):
        if(bc+z<=wc):
            return(b*bc+w*(bc+z))
        else:
            return(b*bc+w*wc)
    elif(wc<bc):
        if(wc+z<=bc):
            return(b*(wc+z)+w*wc)
        else:
            return(b*bc+w*wc)
    
    
print(taumBday(5,9,2,3,4))