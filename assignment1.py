# -*- coding: utf-8 -*-
"""
Created on Sat Nov  1 19:50:21 2025

@author: cansa
"""
import numpy as np


g = 9.81  # in m/s^2
def find_period (Length): 
        T=2*np.pi*((Length/g)**(1/2))
        return T
    
Lmin = int (input("insert minimum length: ")) # in meters 
Lmax = int (input("insert maximum length: ")) # in meters
if (Lmax<Lmin):
    print ("maximum length should be greater than minimum")
else:
    for y in range(Lmin, Lmax +1, 1):
        T=find_period (y) 
        print ("When L = ", float (y), "m, T = ", round(T, 1) ,"s")
        

        