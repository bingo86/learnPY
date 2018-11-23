#!/usr/bin/python
#-*-coding utf-8
def fib(max):
    n,a,b=0,0,1     #此赋值语句相当于t=(0,0,1)，n=t[0] a=t[1] b=t[2]
    while n < max:
        print(b)
        a,b=b,a+b   #此赋值语句相当于t=(b,a+b)，a=t[0] b=t[1]
        n=n+1
    return 'Done'

