"""
list
Version: 0.1
Author: slynxes
Date: 2018-12-06
"""


def main():
    # 列表赋值
    list1 = [1, 3, 5]
    list2 = ['nice', 10, 20.5, (1, 2, 3)]

    # 转为列表
    # list()
    a = (1, 2, 3)
    b = list(a)

    """
    增
    """
    # 插入
    # list.insert(index, value)
    list1.insert(0, 10)

    # 追加
    # list.append(value)
    list1.append(20)

    # 扩展
    # list.extend(iterable)
    list1.extend([10, 20, 30, 40])

    """
    查
    """
    # 根据索引查值
    print(list1[3])
    print(list1[::2])

    # 根据值查索引
    print(list1.index(10))

    """
    改
    """
    list1[2] = 99

    """
    删
    """
    # 根据索引删
    del list1[1]

    # 根据值删
    list1.remove(10)

    # 弹出最后一个元素，返回弹出的值
    list1.pop()

    """
    统计
    """
    # 统计元素的个数
    list1.count(10)
    # 长度
    print(len(list1))
    # 求最大值
    print(max(list1))
    # 求最小值
    print(min(list1))

    """
    排序
    """
    # list.sort(reverse=True)
    list1.sort(reverse=True)

    # sorted(iterable, key=)
    new_list = sorted(list1)
    print(new_list)

    """
    反转
    """
    list1.reverse()

    """
    列表合并
    """
    list2 = list1 + list1
    list3 = list1 * 5
    print(list2)
    print(list3)

    """
    清空列表
    """
    list1.clear()

    # 列表生成器创建列表
    list3 = [x for x in range(10)]
    print(list3)

    list4 = [x ** 2 for x in range(0, 10, 2)]
    print(list4)

    # 下面的方法是创建一个生成器对象，而不是列表
    iterable = (x for x in range(10))
    print(type(iterable))

    """
    列表解析
    [expression for x in iterable]
    [expression for x in iterable if expression2]
    [expression for x in iterable1 for y in iterable2]
    """
    list1 = [1, 3, -2, 9, -10]
    # 去除列表中的负数
    n_list1 = [x for x in list1 if x > 0]
    # 求列表元素的平方
    n_list2 = [x**2 for x in list1]


if __name__ == '__main__':
    main()