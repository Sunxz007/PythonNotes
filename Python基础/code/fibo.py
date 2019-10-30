'''
@Description: 
@Author: 孙晓昼
@since: 2019-10-30 10:11:14
@LastEditors: 孙晓昼
@LastEditTime: 2019-10-30 10:11:23
'''
# 斐波那契(fibonacci)数列模块
 
def fib(n):    # 定义到 n 的斐波那契数列
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()
 
def fib2(n): # 返回到 n 的斐波那契数列
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result