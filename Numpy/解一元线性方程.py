# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 22:01:28 2018

@author: chao
"""

'''
解一元线性方程
x + 2y +  z = 7
2x -  y + 3z = 7
3x +  y + 2z =18
'''
import numpy as np
A=np.array([[1,2,1],[2,-1,3],[3,1,2]])#系数矩阵
print(A)

B=np.array([7,7,18])
print(B)

x=np.linalg.solve(A,B)#解算一元线性方程
print(x)

print(np.dot(A,x))#检验正确性，结果为B
#检测两个矩阵是否相同
print(np.allclose(np.dot(A,x),B))