# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 22:12:21 2018

@author: chao
"""

import numpy as np
x=np.diag((1,2,3))
print(x)

a,b=np.linalg.eig(x)#特征值保存在a中，特征向量保存在b中
print(a)
print(b)
print(a*b)
print(np.dot(a,b))
print("检验特征值与特征向量")
print(np.allclose((a*b),x))
print(np.allclose(np.dot(a,b),x))
