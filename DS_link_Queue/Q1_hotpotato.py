#!/usr/bin/env/ python
# -*— coding=utf-8 -*-
# @FileName :Q1_hotpotato.py
# @Time :2020/8/5 
# @Author: chaofei_liu

from DS_link_set.DS_link_Queue.Queue import Queue

def hotpotato(namelist,num):
    q = Queue()
    for name in namelist:
        q.enqueue(name)
    while q.size() > 1:
        for i in range(num):
            q.enqueue(q.dequeue())

        q.dequeue()

    return q.dequeue()

if __name__ == '__mian__':
    print(hotpotato(['bill','carr','amy','dany','jennfinny','poxrk','eqw','ewqq','weqw'],7))
