#!/usr/bin/python
#-*-coding utf8-*-
def testfilter(s):

    def delOdd(n):
        return n%2==1
    return list(filter(delOdd,s))
