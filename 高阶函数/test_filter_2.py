#!/usr/bin/python
# -*- coding:utf-8 -*-
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n
def _not_divisible(n):
    return lambda x: x % n > 0
def primes():
    yield 2
    it = _odd_iter()  # 初始化序列
    while True:
        n = next(it)  # 返回序列第一个数
        yield n 
        it = filter(_not_divisible(n), it)  #  构造新序列
def main_filter():
    for n in primes():
        if n < 1000:
            print(n)
        else:
            break
