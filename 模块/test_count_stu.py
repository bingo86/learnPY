#!/usr/bin/python
# -*-coding:utf-8-*-
class Student(object):
    count = 0

    def __init__(self,name):
        self.__name = name
        Student.count+=1
    def get_count_stu(object):
        return object.count
        
