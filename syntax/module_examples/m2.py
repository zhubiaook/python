"""
module m2

Version: 0.1
Author: slynxes
Date: 2019-01-23
"""


def who_am_i():
    print("I'm module m2")


class Student(object):
    def __init__(self, name, score):
        self._name = name
        self._score = score

    def print_score(self):
        print(f'm2: name = {self._name}, score = {self._score}')