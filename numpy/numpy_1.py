# -*- coding: utf8 -*-
'''
@Description: 
@Author: 孙晓昼
@since: 2019-10-29 21:34:15
@LastEditors: 孙晓昼
@LastEditTime: 2019-10-29 22:00:59
'''

import numpy

word_alcohol=numpy.genfromtxt("world_alcohol.txt",delimiter=',',dtype=str)
print(type(word_alcohol))
""" print(word_alcohol) """

d=word_alcohol[1]
print(d)
vector=numpy.array([5,10,15.7,20])

matrix=numpy.array([[1,5,21],[34,39,45]])
print(vector)
print(matrix.shape)