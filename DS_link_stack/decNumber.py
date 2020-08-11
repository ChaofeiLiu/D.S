#!/usr/bin/env/ python
# -*— coding=utf-8 -*-
# @FileName :decNumber.py
# @Time :2020/8/4 
# @Author: chaofei_liu
from DS_link_set.DS_link_stack.Stack_for_list import Stack

'''
def divideBy2(decnumber):
    remstack = Stack()
    while decnumber >0:
        rem = decnumber % 2
        remstack.push(rem)
        decnumber = decnumber // 2
    binstring = ''
    while not remstack.is_Empty():
        binstring = binstring + str(remstack.pop())
    return binstring

print(divideBy2(233))
'''
def baseconvert(basenumber,base):
    digits = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    remstack = Stack()
    while basenumber >0 :
        rem = basenumber % base
        remstack.push(rem)
        basenumber = basenumber // base
    basestring = ''
    while not remstack.is_Empty():
        basestring = basestring + digits[remstack.pop()]
    return basestring

print(baseconvert(199,16))




