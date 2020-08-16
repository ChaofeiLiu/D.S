#!/usr/bin/env/ python
# -*— coding=utf-8 -*-
# @FileName :Bubble_sort.py
# @Time :2020/7/30 
# @Author: chaofei_liu

def Bubble_sort(input_list):
    for i in range(len(input_list)):
        for j in range(1,len(input_list)):
            if input_list[j-1] > input_list[j]:
                input_list[j-1],input_list[j] = input_list[j],input_list[j-1]
    return input_list

if __name__ == '__main__':
    list = [1,5,3,2,4,7,6,9,8]
    Bubble_sort(list)
    print(list)


