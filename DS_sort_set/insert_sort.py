#!/usr/bin/env/ python
# -*— coding=utf-8 -*-
# @FileName :insert_sort.py
# @Time :2020/8/16 
# @Author: chaofei_liu

def insert_sort(alist):
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index
        while position >0 and alist[position-1] > currentvalue:
            alist[position] = alist[position-1]
            position = position-1

        alist[position] = currentvalue
    return alist
print(insert_sort([12,2,3,4,7,6,90,34]))
