#!/usr/bin/python
# -*-coding:utf-8-*-
import logging
logging.basicConfig(level=logging.INFO)  # 指定log运行级别，有debug、info、warning、error当指定level为info级别时，logging.debug就不起作用
def foo(s):
    # n = int(s)
    s = '0'
    n = int(s)
    logging.info('n=%d' % n)
    print(10 / n)
    # assert n != 0, 'n is zero'
    # return 10 / n
def main():
    foo('3')
main()
