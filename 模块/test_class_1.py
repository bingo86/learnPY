#!/usr/bin/python
# -*-coding:utf-8 -*-

'''定义Student类'''

class Student(object): 
    def __init__(self,name,gender,score):
        #self.name = name  # 为name属性赋值
        #self.score = score  # 为score属性赋值
        self.__name = name  # 将name属性设置为私有属性，此时外部将无法直接访问
        self.__score = score
        self.__gender = gender
    # 当分数不在范围内时可以设置属性值
    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')
    def get_score(self):
        return self.__score
    def set_name(self, name):
        self.__name = name
    def get_name(self):
        return self.__name
    def set_gender(self, gender):
        self.__gender = gender
    def get_gender(self):
        return self.__gender
    # 打印姓名和分数信息
    def print_score(self):
        print('%s:%s:%s' % (self.__name,self.__gender,self.__score))
    # 通过分数判定返回级别
    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >=60:
            return 'B'
        else:
            return 'C'

