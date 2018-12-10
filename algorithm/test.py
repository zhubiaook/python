"""
Description

Version: 0.1
Author: Slynxes
Date: 2018-12-06
"""


class Person:
    name = 'zhubiao'

    def __init__(self, name):
        self.name = name
        print('Haha')

    def get_name(self):
        return self.name


if __name__ == '__main__':
    per = Person('Slnxyes')
    print(per.name)