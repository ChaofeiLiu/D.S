#!/usr/bin/env/ python
# -*— coding=utf-8 -*-
# @FileName :Queue.py
# @Time :2020/8/5 
# @Author: chaofei_liu

class Queue():
    def __init__(self):
        self.itmes = []

    def is_empty(self):
        return self.itmes == []

    def enqueue(self,item):
        self.itmes.insert(0,item)

    def dequeue(self):
        return self.itmes.pop()

    def size(self):
        return len(self.itmes)

if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())