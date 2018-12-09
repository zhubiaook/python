"""
dictionary
Version: 0.1
Author: slynxes
Date: 2018-12-09
"""


def main():
    """
    dictionary
    :return:
    """
    # 常规
    s = {'zb': 100, 'zy': 90, 'hdx': 80}
    print(len(s))
    print(max(s))
    print(min(s))
    print(s.clear())

    # 增加或修改
    s1 = {'zb': 100, 'zy': 90, 'hdx': 80}
    pass
    s1['zb'] = 150
    s1['zpp'] = 68
    s1.update(xc=85, cls=80)
    print(s1)

    # 读取
    for elem in s1:
        print(elem)

    print(s1.get('zb', 30))
    print(s1['zb'])
    print(s1.keys())
    print(s1.values())
    print(s1.items())
    for x, y in s1.items():
        print(x, y)

    # 删除
    print(s1)
    del s1['xc']
    print(s1)
    print(s1.pop('hdx'))
    print(s1.popitem())


if __name__ == '__main__':
    main()