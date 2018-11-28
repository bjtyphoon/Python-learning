# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 21:10:36 2018

@author: chao
"""

import numpy as np
A=np.array([[1,-2,1],[0,2,-1],[1,1,-2]])
print(A)
A_det=np.linalg.det(A)#求A的行列式，不为零则存在逆矩阵
print(A_det)
A_inverse = np.linalg.inv(A)#A_inverse
print(A_inverse)
print(np.dot(A,A_inverse))#A与其逆矩阵的乘积为单位阵
A_companion=A_inverse*A_det#求A的伴随矩阵
print(A_companion)