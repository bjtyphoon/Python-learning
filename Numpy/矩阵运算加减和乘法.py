# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 17:50:57 2018

@author: chao
"""
import numpy as np
#使用mat函数
print("矩阵")
A = np.mat([[1,2,3],[4,5,6],[7,8,9]])
B = np.matrix([[9,8,7],[6,5,4],[3,2,1]])
#注意A, B都是matrix类型，可以使用乘号，如果是array则不可以直接使用乘号
print(A)
print(B)
print(A+B)
print(A-B)
#矩阵乘法  行*列
print(A*B)

print("数组")
C= np.array([[1,2,3],[4,5,6],[7,8,9]])
D= np.array([[9,8,7],[6,5,4],[3,2,1]])
print(C)
print(D)
print(C+D)
print(C-D)
print(C*D)#数组乘法不是矩阵乘法
print(np.dot(C,D))

print("线性代数维数")
E=np.array([1,2,3])
F=np.array([9,8,7])
print(E.shape)
'''
数组dot运算在一维数组是内积,
线代中提到的n维行向量在Python中是一维数组，
线代中的n维列向量在Python中是一个shape为(n, 1)的二维数组
矩阵乘法内标相同，外标为结果行列数
'''
print(np.dot(E,F))
print(np.dot(F,E))

G=F.reshape(-1,1)
print(G)
print(G.shape)
#因此dot(F, G)不再是内积，而是一个只有一个元素的数组
print(np.dot(F,G))
#print(np.dot(G,F))  ValueError: shapes (3,1) and (3,) not aligned: 1 (dim 1) != 3 (dim 0)
E.shape=(1,-1)
print(E.shape)
print(np.dot(G,E))
print(np.dot(E,G))