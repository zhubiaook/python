"""
module m1

Version: 0.1
Author: slynxes
Date: 2019-01-23
"""


def who_am_i():
    return "I'm module m1"


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print(f'm1: name = {self.name}, score = {self.score}')

