# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 21:47:50 2018

@author: chao
"""

import random
print('莫西莫西，我们来玩个小游戏啊，猜猜我心里想的数字')
guess = random.randint(1, 10)
print(guess)
num = int(input('数字是1-10的整数哦\n'))
i = 0
while i <2:
    if num > guess:
        i += 1
        num = int(input('哎呀，大了大了，重新输入\n'))
        continue
    if num < guess:
        i += 1
        num = int(input('哎哟，小了小了，重新输入\n'))
        continue
    else:
        print('猜对啦')
        print('游戏结束')
        break
if num==guess and i >= 2:
    print('猜对啦')
    print('游戏结束')
if num != guess and i >= 2:
    print('还是错啦，超过三次咯，没得玩咯')

