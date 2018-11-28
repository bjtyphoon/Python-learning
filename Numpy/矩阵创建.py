# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 17:45:51 2018

@author: chao
"""

import numpy as np
#使用mat函数创建一个2X3矩阵
a=np.mat([[1,2,3],[4,5,6]])
print(a)
 #使用matrix函数创建一个2X3矩阵
b=np.matrix([[1,2,3],[4,5,6]])
print(b)
print(a.shape)
#使用二维数组代替矩阵
c=np.array([[1,2,3],[4,5,6]])
print(c)
print(type(c))
#方阵
I=np.eye(5)
print(I)