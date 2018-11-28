# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 21:40:58 2018

@author: chao
"""

import numpy as np
A=np.array([[0,-1],[1,0]])
B=np.array([[1,1],[1,1]])
C=A-B  #计算欧式距离矩阵C
print(C)
D=np.dot(C,C)#距离矩阵的平方
print(D)
E=np.trace(D)#计算矩阵D的迹
print(E)
print(E**0.5)
