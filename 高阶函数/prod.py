#!/usr/bin/python
#-*-coding utf8-*-
def prod(L):
    def cheng(x,y):
        return x*y
    return reduce(cheng,L)

