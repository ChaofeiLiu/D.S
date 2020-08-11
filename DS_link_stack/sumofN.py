#!/usr/bin/env/ python
# -*— coding=utf-8 -*-
# @FileName :sumofN.py
# @Time :2020/8/4 
# @Author: chaofei_liu

def sumofN(n):
    index = 0
    sum = 0
    while index <= n:
        sum = sum + index
        index = index +1
    return sum
def sumofN2(n):
    sum = 0
    for i in range(n+1):
        sum = sum + i
    return sum

print(sumofN(eval(input('请输入要求和的正整数:'))))
print(sumofN2(eval(input('请输入要求和的正整数:'))))

