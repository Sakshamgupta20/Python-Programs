# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 19:52:51 2019

@author: Saksham
"""

"""
Julius Caesar protected his confidential information by encrypting it using a cipher. Caesar's cipher shifts each letter by a number of letters. If the shift takes you past the end of the alphabet, just rotate back to the front of the alphabet. In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.

Original alphabet:      abcdefghijklmnopqrstuvwxyz
Alphabet rotated +3:    defghijklmnopqrstuvwxyzabc
"""
import string
def caesarCipher(s, k):
    res=''
    l=list(string.ascii_lowercase)
    for i in range(len(s)):
        if(s[i].isalpha()): 
            nn=l.index(s[i].lower())
            if(nn+k<=25):
                if(s[i].isupper()):
                    res+=l[nn+k].upper()
                else:
                    res+=l[nn+k]
            else:
                m=k
                while(m>=26):
                    m-=26
                if(s[i].isupper()):
                    res+=l[nn+m-26].upper()
                else:
                    res+=l[nn+m-26]
        else:
            res+=s[i]
    return(res)

print(caesarCipher('Hello_World!',4))