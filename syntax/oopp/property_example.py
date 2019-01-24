"""
实例的属性

Version: 0.1
Author: slynxes
Date: 2019-01-24
"""


class Student(object):
    def __init__(self, score):
        self._score = score

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value



