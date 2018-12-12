class Test(object):
    def __init__(self, name, password, course):
        self.name = name
        self.password = password
        self.course = course

    def print_self(self):
        print(self.name, self.password, self.course.sum_course())


class Course(object):
    def __init__(self, english, math):
        self.english = english
        self.math = math

    def sum_course(self):
        return self.english + self.math


class Stu1(object):
    def __call__(self):
        return self


class Stu2(object):
    def __init__(self):
        pass


if __name__ == '__main__':
    s1 = Stu1()


