# -*- coding: utf8 -*-
'''
@Description: 
@Author: 孙晓昼
@since: 2019-10-29 21:34:15
@LastEditors: 孙晓昼
@LastEditTime: 2019-10-31 15:22:49
'''

import numpy as np

a = np.arange(24) 
print(a) 
print (a.ndim)         # a 现只有一个维度
# 现在调整其大小
b = a.reshape(2,4,3)  # b 现在拥有三个维度
print (b.ndim)