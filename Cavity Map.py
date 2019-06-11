# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 19:58:02 2019

@author: Saksham
"""


"""
You are given a square map as a matrix of integer strings. Each cell of the map has a value denoting its depth. We will call a cell of the map a cavity if and only if this cell is not on the border of the map and each cell adjacent to it has strictly smaller depth. Two cells are adjacent if they have a common side, or edge.

Find all the cavities on the map and replace their depths with the uppercase character X.

For example, given a matrix:
    
989         989
191-------> 1X1
111         111
"""

def cavityMap(grid):
    grid1=[]
    for i in grid:
        grid1.append(list(i))
    for i in range(1,len(grid)-1):
        for j in range(1,len(grid)-1):
            if grid1[i][j]>max(grid1[i-1][j],grid1[i+1][j],grid1[i][j-1],grid1[i][j+1]):
                grid1[i][j]='X'
    x=[]
    for i in range(len(grid1)):
        x.append(''.join(grid1[i]))
    print(x)
cavityMap(['1112','1912','1892','1234'])
    