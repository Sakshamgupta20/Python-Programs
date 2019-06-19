# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 16:46:03 2019

@author: Saksham
"""
"""
You will be given a square chess board with one queen and a number of obstacles placed on it. Determine how many squares the queen can attack.

A queen is standing on an n * n chessboard. The chess board's rows are numbered from 1 to n, going from bottom to top. Its columns are numbered from 1 to n, going from left to right. Each square is referenced by a tuple,(r,c) , describing the row, r, and column, c, where the square is located.

The queen is standing at position(rq,cq) . In a single move, she can attack any square in any of the eight directions (left, right, up, down, and the four diagonals).


Complete the queensAttack function in the editor below. It should return an integer that describes the number of squares the queen can attack.

queensAttack has the following parameters: 
- n: an integer, the number of rows and columns in the board 
- k: an integer, the number of obstacles on the board 
- r_q: integer, the row number of the queen's position 
- c_q: integer, the column number of the queen's position 
- obstacles: a two dimensional array of integers where each element is an array of 2 integers, the row and column of an obstacle

https://www.hackerrank.com/challenges/queens-attack-2/problem
"""

def queensAttack(n, k, r_q, c_q, obstacles):
    ver_u=n-r_q
    ver_l=r_q-1
    hori_l=c_q-1
    hori_u=n-c_q
    diag_u1=min(ver_u,hori_l)
    diag_u2=min(ver_u,hori_u)
    diag_l1=min(ver_l,hori_l)
    diag_l2=min(ver_l,hori_u)
    
    for i in obstacles:
        r=i[0]
        c=i[1]
        if(r==r_q):
            if(c<c_q):
                hori_l=min(hori_l,c_q-c-1)
            else:
                hori_u=min(hori_u,c-1-c_q)
        elif(c==c_q):
            if(r<r_q):
                ver_l=min(ver_l,r_q-r-1)
            else:
                ver_u=min(ver_u,r-r_q-1)
        elif(abs(r-r_q)==abs(c_q-c)):
            if(r>r_q and c<c_q):
                diag_u1=min(diag_u1,c_q-c-1)
            elif(r>r_q and c>c_q):
                diag_u2=min(diag_u2,c-c_q-1)
            elif(r<r_q and c<c_q):
                diag_l1=min(diag_l1,c_q-c-1)
            elif(r<r_q and c>c_q):
                diag_l2=min(diag_l2,c-c_q-1)
    
    return(ver_u+ver_l+hori_l+hori_u+diag_l1+diag_l2+diag_u1+diag_u2)


print(queensAttack(8,1,4,4,[[5,1]]))
