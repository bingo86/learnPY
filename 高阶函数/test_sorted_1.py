#!/usr/bin/python
# -*-coding:utf-8 -*-
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def sortByName(t):
    for name,score in t:
        print(name)
#sorted(L,key=sortByName)
def by_name(t):
    return t[0].lower
def by_score(t):
    return t[1]
print(list(sorted(L,key=by_name)))
print(list(sorted(L,key=by_score)))


