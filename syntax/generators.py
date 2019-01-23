"""
生成器
    生成器中的元素不像列表一样预先存储于内存中，
    而是在被访问时通过某种算法推算出后续元素，
    从而节省大量内存空间

Version: 0.1
Author: slynxes
Date: 2019-01-19
"""


def print_num():
    """
    yield 与其他函数不同之处在于，其他函数遇到return或最后一行时返回
    而 yield每次调用next()时执行，遇到yield返回，下次执行是从上次yield返回处继续。
    :return:
    """
    print('step_1 ')
    yield 1
    print('step_2 ')
    yield 2
    print('step_3')
    yield 3


def fib(max_num):
    for i in range(max_num):
        yield [i * i, i + i]


def triangles(row):
    """
    杨辉三角形
    :param row:
    :return:
    """
    for line_num in range(1, row+1):
        if line_num == 1:
            pre_list = [1]
            yield pre_list
        else:
            cure_list = []
            for i in range(line_num):
                if i == 0:
                    cure_list.append(0 + pre_list[i])
                elif i == line_num - 1:
                    cure_list.append(pre_list[i-1] + 0)
                else:
                    cure_list.append(pre_list[i-1] + pre_list[i])
            pre_list = cure_list
            yield cure_list


if __name__ == '__main__':
    for item in triangles(10):
        print(item)
