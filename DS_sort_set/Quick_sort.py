#!/usr/bin/env/ python
# -*— coding=utf-8 -*-
# @FileName :Quick_sort.py
# @Time :2020/7/30 
# @Author: chaofei_liu

def Quick_sort(input_list):
    Quicksorthelper(input_list,0,len(input_list)-1)

def Quicksorthelper(input_list,first,last):
    if first < last:
        splitpoint = partition(input_list,first,last)
        Quicksorthelper(input_list,first,splitpoint-1)
        Quicksorthelper(input_list,splitpoint+1,last)

def partition(list,first,last):
    pivotvalue = list[first]
    leftmark = first+1
    rightmark = last
    done = False
    while not done:
        #  移动左标
        while leftmark <= rightmark and list[leftmark] <= pivotvalue:
            leftmark = leftmark +1
        # 移动右标
        while leftmark <= rightmark and list[rightmark] >= pivotvalue:
            rightmark = rightmark -1
        # 右标值小于左标值退出
        if rightmark < leftmark:
            done = True
        # 交换左右的值（左大于基准值，右小于基准值）
        else:
            temp = list[leftmark]
            list[leftmark] = list [rightmark]
            list[rightmark] = temp
    # 循环结束  此时第一个数为中值，和右标的位置互换，中值归为，排序结束。右标点为中值点
    temp = list[first]
    list[first] = list[rightmark]
    list[rightmark] = temp
    return rightmark

input = [1,2,34,5567,88,77,33,80,31]
Quick_sort(input)
print(input)


