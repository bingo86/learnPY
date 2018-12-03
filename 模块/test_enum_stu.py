#!/usr/bin/python
# -*-coding:utf-8-*-
from enum import Enum,unique
class Gender(Enum):
    Male = 0
    Female = 1
class Student(object):
    def __init__(self,name,gender):
        self.name = name
        if isinstance(gender,Gender):
            self.gender = gender
        else:
            print("gender must be Gender type.")
            return 0
#
#    @property
#    def gender(self):
#        return self.gender
#    @property
#    def name(self):
#        return self.name
#    @name.setter
#    def name(self, value):
#        self.name = value





