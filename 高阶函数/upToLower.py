#!/usr/bin/python
#-*-coding utf8 -*-
def upToLower(s):
    def capti(x):
        return x.capitalize()
    return map(capti,s)

