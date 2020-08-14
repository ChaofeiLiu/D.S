#!/usr/bin/env/ python
# -*— coding=utf-8 -*-
# @FileName :q4.py
# @Time :2020/8/14 
# @Author: chaofei_liu

# 汉诺塔问题

def movetower(height,frompole,withpole,topole):
    if height >= 1:
        movetower(height-1,frompole,topole,withpole)
        movedisk(height,frompole,topole)
        movetower(height-1,withpole,frompole,topole)

def movedisk(disk,fromple,topole):
    print(f'moving disk[{disk}] form {fromple} to {topole}')

movetower(3,'#1','#2','#3')



