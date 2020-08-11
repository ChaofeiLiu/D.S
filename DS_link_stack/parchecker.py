#!/usr/bin/env/ python
# -*— coding=utf-8 -*-
# @FileName :parchecker.py
# @Time :2020/8/4
# @Author: chaofei_liu

from DS_link_set.DS_link_stack.Stack_for_list import Stack

'''  圆括号匹配算法
def parchecker(input_string):
    s = Stack()
    flag = True
    index = 0
    while index < len(input_string) and flag:
        symbol = input_string[index]
        if symbol == '(':
            s.push(symbol)
        else:
            if s.is_Empty():
                flag = False
            else:
                s.pop()
        index = index + 1
    if s.is_Empty() and flag:
        return True
    else:
        return False

print(parchecker('(())'))
print(parchecker('(()))'))
print(parchecker('())'))
'''

def parchecker(input_string):
    s = Stack()
    flag = True
    index = 0
    while index < len(input_string) and flag:
        symbol = input_string[index]
        if symbol in '([{':
            s.push(symbol)
        else:
            if s.is_Empty():
                flag = False
            else:
                top = s.pop()
                if not matches(top,symbol):
                    flag = False
        index = index + 1
    if s.is_Empty() and flag:
        return True
    else:
        return False

def matches(open,close):
    opens = '([{'
    closers = ')]}'
    return opens.index(open) == closers.index(close)

print(parchecker('([}({}))'))
print(parchecker('([{}])'))
print(parchecker('{[)}])'))