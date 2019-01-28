"""
类间关系
    依赖
    聚合
    继承

Version: 0.1
Author: slynxes
Date: 2019-01-25
"""


class Student(object):
    __slots__ = ('_id', '_name', '_score')

    def __init__(self):
        self._name = 1

    def run(self):
        print('Student run' + str(self._name))


class Sportsman(object):
    pass


class HighSchoolStudent(Student):
    def __init__(self):
        Student.__init__(self)

    __slots__ = Student.__slots__ + ('_course', )
    pass


class CollegeStudent(Student):
    def __init__(self):
        Student.__init__(self)

    def run(self):
        print('College student run' + str(self._name))

    __slots__ = Student.__slots__ + ('_computer', '_physical')
    pass


class SecondClassStudent(HighSchoolStudent, Sportsman):
    __slots__ = HighSchoolStudent.__slots__ + CollegeStudent.__slots__
    pass
