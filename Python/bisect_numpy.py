# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 09:57:49 2022

@author: miarcos
"""

def f(x):
    return (x-1)*(x+2)

a = 0.1
b = 1.5
TOL = 1E-2

assert f(a)*f(b) < 0;"a função deve mudar de sinal"

while((b-a)/2 > TOL):
    p = (a + b)*0.5
    
    if( f(a) * f(p) < 0 ):
        b = p
    elif( f(b) * f(p) < 0):
        a = p