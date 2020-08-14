#!/usr/bin/env/ python
# -*— coding=utf-8 -*-
# @FileName :q2.py
# @Time :2020/8/14 
# @Author: chaofei_liu

#任意进制转换问题（递归解决）

def tostr(n,base):
    table = '0123456789ABCDEF'
    if n < base:
        return table[n]
    else:
        return tostr(n//base,base) + table[n%base]
print(tostr(17,8))
