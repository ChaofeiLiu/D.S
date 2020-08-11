#!/usr/bin/env/ python
# -*— coding=utf-8 -*-
# @FileName :postfixeval.py
# @Time :2020/8/5 
# @Author: chaofei_liu

from DS_link_set.DS_link_stack.Stack_for_list import Stack

def postfixeval(input_strings):
    s = Stack()
    tokenlist = input_strings.split()
    print(tokenlist)
    for token in tokenlist:
        if token in '0123456789':
            s.push(int(token))
        else:
            op2 = s.pop()
            op1 = s.pop()
            result = domath(token,op1,op2)
            s.push(result)
    return s.pop()

def domath(op,op1,op2):
    if op == '+':
        return op1 + op2
    elif op == '-':
        return op1 - op2
    elif op == '*':
        return op1 * op2
    else:
        return op1 / op2

if __name__ == '__main__':
    print(postfixeval(input('请输入要求值的后缀表达式（用空格隔开）:')))