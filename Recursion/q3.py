#!/usr/bin/env/ python
# -*— coding=utf-8 -*-
# @FileName :q3.py
# @Time :2020/8/14 
# @Author: chaofei_liu

#turtle递归可视化显示

import turtle

def koch(size, n):
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0, 60, -120, 60]:
            turtle.left(angle)
            koch(size / 3, n - 1)

def main():
    turtle.setup(600, 600)
    turtle.penup()
    turtle.goto(-200, 100)
    turtle.pendown()
    turtle.pencolor("purple")
    turtle.pensize(2)
    level = 4
    koch(400, level)
    turtle.right(120)
    koch(400, level)
    turtle.right(120)
    koch(400, level)
    turtle.hideturtle()

main()