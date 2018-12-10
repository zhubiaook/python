"""
Just a test
Version: 0.0
Author: slynxes
Date: 2018-12-01
"""


def main():
    pass


def num():
    for i in range(10):
        yield i


if __name__ == '__main__':
    for x in num():
        print(x)
