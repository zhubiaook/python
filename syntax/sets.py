"""
set
Version: 0.1
Author: slynxes
Date: 2018-12-09
"""


def main():
    set1 = {1, 3, 5, 7}
    set2 = {1, 2, 3, 4, 5}
    set3 = {3, 7}

    # 通用
    print(len(set1))
    print(max(set1))
    print(min(set1))
    list1 = [1, 3, 5]
    print(set(list1))
    print(set1.add(11))
    print(set1.pop())
    print(set1.remove(11))
    print(set3.clear())

    # 交集
    print(set1 & set2)
    print(set1.intersection(set2))
    # 交集并赋值
    print(set1.intersection_update(set2))

    # 并集
    print(set1 | set2)
    print(set1.union(set2))

    # 差集
    print(set1 - set2)
    print(set1.difference(set2))
    print(set1.difference_update(set2))

    # 对称集
    print(set1 ^ set2)
    print(set1.symmetric_difference(set2))
    print(set1.symmetric_difference_update(set2))

    # 子集或超集
    print(set1 <= set2)
    print(set1.issubset(set2))

    print(set1 >= set2)
    print(set1.issubset(set2))


if __name__ == '__main__':
    main()