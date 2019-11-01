# -*- coding: utf8 -*-
'''
@Description: 
@Author: 孙晓昼
@since: 2019-10-29 21:34:15
@LastEditors: 孙晓昼
@LastEditTime: 2019-10-31 15:22:49
'''

import numpy as np
 
a = np.array([[1,2,3], [4,5,6],[7,8,9]])
print(a)
b = a[0:2, 1:3]
c = a[1:3,[1,2]]
d = a[...,1:]
print(b)
print(c)
print(d)

print(a[0:2])