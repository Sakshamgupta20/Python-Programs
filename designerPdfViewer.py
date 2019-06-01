# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 18:10:25 2019

@author: Saksham
"""
import string
def designerPdfViewer(h, word):
    keys=list(string.ascii_lowercase)
    x=dict(zip(keys,h))
    return(int(max(x[i] for i in word))*len(word))
    
    
print(designerPdfViewer('1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 7'.split(" "),'zaba'))