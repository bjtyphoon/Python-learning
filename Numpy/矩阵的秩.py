# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 21:57:59 2018

@author: chao
"""

import numpy as np
I=np.eye(3) #先创建一个单位阵
print(I)
I_rank=np.linalg.matrix_rank(I)#秩
print(I_rank)
I[1,1]=0
print(I)
I_rank=np.linalg.matrix_rank(I)#秩
print(I_rank)