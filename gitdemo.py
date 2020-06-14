#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 08:26:36 2020

@author: jiaoguoning
"""
import numpy as np
import matplotlib.pyplot as plt

# 需求：画一个线形图
print('hello')
print('我在github做了更改')
print('我在本地仓库做了更改')

b = np.array([1,2,3,4,5,6])
y = b * 0.89 

plt.plot(b, y, 'r--')
plt.xlabel('x轴')
plt.ylabel('y轴')
plt.title('需求线形图')
plt.show()

@timer 
print('hello word!')
