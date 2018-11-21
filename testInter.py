#!/usr/bin/python
#-*-coding utf-8-*-
#s=[13,20,10,14,32,15]
def findMinAndMax(s):
    if s ==[]:
        return (None,None)
    max=s[0]
    min=s[0]
    for mid in s:
        if max<mid:
            max=mid
        if min>mid:
            min=mid
    return(max,min)
#findMinAndMax(s)
