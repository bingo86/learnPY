#!/usr/bin/python
# -*-coding:utf-8-*-

'''使用@property来将类中的方法变成属性来调用'''
class Student(object):
    # __slots__ = ('name','age')

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100!')
        self._score = value

'''定义get和set方法来将类属性对外部隐藏'''
#class Student(object):
#    def get_score(self):
#        return self._score
#    def set_score(self, score):
#        if not isinstance(score, int):
#            raise ValueError("score must be an integer!")
#        if score < 0 or score > 100:
#            raise ValueError("score must between 0~100!")
#        self._score = score
#
