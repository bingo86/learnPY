#!/usr/bin/python
# -*-coding:utf-8 -*-
import logging
def foo(s):
    return 10 / int(s)
def bar(s):
    return foo(s) * 2
def main(s):
    try:
        print(bar(s))
    except Exception as e:
        # print('Error: ', e)
        logging.exception(e)
    finally:
        print('END')
main(0)
