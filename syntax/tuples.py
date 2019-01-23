"""
tuples
Version: 0.1
Author: slynxes
Date: 2018-12-09
"""


def main():
    tuple1 = (1, 2, 3, 4, 5)
    tuple2 = (10, 20, 30, 40, 50)

    # 取值
    print(tuple1[0])
    print(tuple1[2:4])
    print(tuple1[2:len(tuple1)])
    for i in tuple1:
        print(i)

    # 运算
    print(tuple1 + tuple2)
    print(tuple1 * 2)

    # 比较
    print(len(tuple1))
    print(max(tuple1))
    print(min(tuple1))

    # 转换
    list1 = [10, 20, 30]
    str1 = "Hello, World"
    print(tuple(list1))
    print(tuple(str1))

    # 案例
    def score(*args):
        """
        args为任意元素组成的元祖
        :param args:
        :return:
        """
        print(args)

    score(1, 2, 'English')


if __name__ == '__main__':
    main()
