#!/usr/bin/env/ python
# -*— coding=utf-8 -*-
# @FileName :q1.py
# @Time :2020/8/14 
# @Author: chaofei_liu

def listsum(listnum):
    if len(listnum) ==1:
        return  listnum[0]
    else:
        return listnum[0] + listsum(listnum[1:])

print(listsum([1,2,3,4,5]))
