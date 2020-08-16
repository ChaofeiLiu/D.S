#!/usr/bin/env/ python
# -*— coding=utf-8 -*-
# @FileName :binarysearch.py
# @Time :2020/8/16 
# @Author: chaofei_liu

# 普通实现
def binarysearch(alist,item):
    first = 0
    last = len(alist) - 1
    found = False
    while first <= last and not found:
        midpoint = (first+last) // 2
        if alist[midpoint] == item:
            found = True
        else:
            if alist[midpoint] > item:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return found

# 递归写法

def binarysearch2(alist,item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist) // 2
        if alist[midpoint] == item:
            return True
        else:
            if alist[midpoint] < item:
                return binarysearch2(alist[midpoint+1:],item)
            else:
                return binarysearch2(alist[:midpoint],item)

inputlist = [1,2,3,5,6,8,9]
print(binarysearch(inputlist,11))
print(binarysearch2(inputlist,10))



