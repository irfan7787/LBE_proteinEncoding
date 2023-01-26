# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 22:33:39 2023

@author: irfan kösesoy
"""

import numpy as np


def LBE(seq, L):
    seqLength = len(seq)
    F = np.zeros((L,40))

    for i in range(1,L+1):
        x = int((i/L)*seqLength)
        S = seq[:x]
        F[i-1,:] = distFeature(S)
    
    F = F.reshape(1,L*40)
    return F

def distFeature(seq):
    n = len(seq)
    f = np.zeros(40)
    aa_code = {'A':0, 'R':1, 'N':2, 'D':3, 'C':4, 'Q':5, 'E':6, 'G':7, 'H':8, 'I':9, 'L':10, 'K':11, 'M':12, 'F':13, 'P':14, 'S':15, 'T':16, 'W':17, 'Y':18, 'V':19}
    for i in range(n):
        v = aa_code[seq[i]]
        f[v] = f[v] + (i+1)/n
        
    s2 = seq[::-1]

    for i in range(n):
        v = aa_code[s2[i]]
        f[v+20] = f[v+20] + (i+1)/n

    return f


