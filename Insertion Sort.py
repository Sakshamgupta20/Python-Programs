# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 21:28:27 2019

@author: Saksham
"""





def insertionSort2(n, arr):
    for i in range(n-1):
        j=i+1
        if arr[j]<arr[i]:
            while(i>0):
                i-=1
                if(arr[i]<=arr[j]):
                    i+=1
                    break
            temp=arr[j]
            del arr[j]
            arr.insert(i,temp)
        print(*arr)   
            
insertionSort2(7,[3,4,7,5,6,2,1])


    
