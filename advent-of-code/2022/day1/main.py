#!/usr/bin/env python3

f = open("input.in", "r")


num = 0
top = [0]


for i in f:
    if i != '\n':
        num += int(i)
    if i == '\n':
        if num > top[len(top) - 1]:
            top.append(num)
        num = 0

print(top[len(top) - 3] + top[len(top) - 2] + top[len(top) - 1])
