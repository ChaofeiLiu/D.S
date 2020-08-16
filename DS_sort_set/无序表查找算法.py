#!/usr/bin/env/ python
# -*— coding=utf-8 -*-
# @FileName :无序表查找算法.py
# @Time :2020/8/16 
# @Author: chaofei_liu

def underlist_search(alist,item):
    pos = 0
    found = False
    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos + 1

    return found

input_list = [1,2,3,4,5,6,7]
print(underlist_search(input_list,6))
print(underlist_search(input_list,9))
