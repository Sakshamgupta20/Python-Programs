# -*- coding: utf-8 -*-
"""
Created on Thu May 23 15:26:28 2019

@author: Saksham
"""

"""
All sorted lowercase letters are ahead of uppercase letters.
All sorted uppercase letters are ahead of digits.
All sorted odd digits are ahead of sorted even digits.
"""

s=input()
digite=[]
digito=[]
lower=[]
higher=[]
for i in s:
    if i.isdigit():
        if int(i)%2==0:
            digite.append(int(i))
        else:
            digito.append(int(i))
    elif(i.islower()):
        lower.append(i)
    else:
        higher.append(i)
s=''.join(str(i) for i in sorted(lower))
s=s+''.join(str(i) for i in sorted(higher))
s=s+''.join(str(i) for i in sorted(digito))     
s=s+''.join(str(i) for i in sorted(digite))  
print(s,end='')  