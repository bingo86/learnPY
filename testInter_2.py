#!/usr/bin/python
#-*-coding utf-8-*-
def findMinAndMax(L):
    if L !=[]:
        (min,max)=(L[0],L[0])
        for x in L:
            if max<x:
                max=x
            if min>x:
                min=x
        return(min,max)
    else:
        return(None,None)
