# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 18:34:01 2018

@author: chao
"""

import numpy as np
A = np.mat([[1,2,3],[4,5,6],[7,8,9]])
B = np.matrix([[9,8,7],[6,5,4],[3,2,1]])

print(A)
print(B)

print(A.T)
print(B.T.T)

#验证矩阵转置的性质：(A±B)'=A'±B'
print(A+B)
print((A+B).T)
print(A.T+B.T)
print(((A+B).T)==(A.T+B.T))
#验证矩阵转置的性质：(KA)'=KA'
print(10*(A.T))
print((10*A).T)
#验证矩阵转置的性质：(A×B)'= B'×A'
print(np.dot(A,B).T)
print(np.dot(B.T,A.T))
