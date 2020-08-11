#!/usr/bin/env/ python
# -*— coding=utf-8 -*-
# @FileName :Stack_for_list.py
# @Time :2020/8/4 
# @Author: chaofei_liu

class Stack():
    def __init__(self):
        self.items = []

    def is_Empty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

'''
test_eg:
print(s.is_Empty())
s.push(1)
s.push(2)
s.push(3)
print(s.size())
print(s.peek())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.size())
'''

