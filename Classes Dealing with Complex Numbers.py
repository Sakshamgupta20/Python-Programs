# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 20:29:46 2019

@author: Saksham
"""

import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real=real
        self.imaginary=imaginary
            
    def __add__(self, no):
        return(Complex(self.real+no.real,self.imaginary+no.imaginary))
        
    def __sub__(self, no):
        return(Complex(self.real-no.real,self.imaginary-no.imaginary))
    def __mul__(self, no):
        a=self.real
        b=self.imaginary
        c=no.real
        d=no.imaginary
        return(Complex((a*c)-(b*d),(a*d)+(b*c)))
    def __truediv__(self, no):
        a=self.real
        b=self.imaginary
        c=no.real
        d=no.imaginary
        m1=((a*c)+(b*d))
        d1=c**2+d**2
        m2=((b*c)-(a*d))
        d2=c**2+d**2
        return(Complex(m1/d1,m2/d2))
    def mod(self):
        a = self.real
        b = self.imaginary
        return Complex(math.sqrt(a**2+b**2),0)
    
    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result
        
if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')

