#!/usr/bin/env/ python
# -*— coding=utf-8 -*-
# @FileName :merge_sort.py
# @Time :2020/8/16 
# @Author: chaofei_liu

def merge_sort(alist):
    if len(alist) <=1:
        return  alist
    else:
        middle = len(alist) // 2
        left = merge_sort(alist[:middle])
        right = merge_sort(alist[middle:])
        merge = []
        while left and right:
            if left[0] <= right[0]:
                merge.append(left.pop(0))
            else:
                merge.append(right.pop(0))
        merge.extend(right if right else left)

    return merge

print(merge_sort([12,22,13,454,78,112,4443,32]))

#  算法复杂度 O（n*log（n））   空间复杂度高

