"""
Description

Version: 0.1
Author: slynxes
Date: 2019-01-23
"""


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print(f'name = {self.name}, score = {self.score}')