#!/usr/bin/python
# -*-coding:utf-8-*-
def createrCounter():
    def f():
        n = 0
        while True:
            n = n + 1
            yield n
    sum = f()
    def counter():
        return next(sum)
    return counter


