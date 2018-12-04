#!/usr/bin/python
# -*-coding:utf-8 -*-

from functools import reduce
import logging

def str2num(s):
    return float(s)
def calc(exp):
    try:
        ss = exp.split('+')
        ns = map(str2num, ss)
    except Exception as e:
        #print('Exception', e)
        logging.exception(e)
    return reduce(lambda acc, x: acc + x, ns)
def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()
