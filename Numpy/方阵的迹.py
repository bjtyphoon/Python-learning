# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 20:57:10 2018

@author: chao
"""

import numpy as np
A= np.array([[1,2,3],[4,5,6],[7,8,9]])
B= np.array([[9,8,7],[6,5,4],[3,2,1]])
print(A)
print(B)
print(np.trace(A))
print(np.trace(A.T))# A的迹等于A.T的迹
print(np.trace(A+B))
print(np.trace(A)+np.trace(B))# 和的迹等于迹的和
print(np.trace((A+B).T))
print(np.trace(A.T)+np.trace(B.T))