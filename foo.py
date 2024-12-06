# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 18:09:30 2024

@author: jiali
"""

def is_divisible_by_k(x,k):
    '''
    Checks whether x is devisible by k
    '''
    assert x%k==0
    
'''
Store all the integers that are multiples of 2 or 5 or 7 that are lower or equal to 1000 (excluding doubles)
'''

x = ()
for i in range(1000):
    if (is_divisible_by_k(x, 2)& is_divisible_by_k(x, 3))| is_divisible_by_k(x, 7):
    x.append(i)

'''

Sum all the integers that are multiples of 2 or 5 or 7 that are lower or equal to 1000 (ecluding doubles)
'''

sum(x) 
   
    Parameters
    ----------
    x : TYPE
        DESCRIPTION.
    k : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    '''