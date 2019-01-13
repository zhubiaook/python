"""
从列表、字典、集合中根据条件筛选数据
Version: 0.1
Author: slynxes
Date: 2019-01-13
"""


def list_screen1(list_data):
    new_list_data = []
    for item in list_data:
        if item >= 0:
            new_list_data.append(item)
    return new_list_data


def is_positive(num):
    return num > 0


def list_screen2(list_data):
    seq_data = filter(is_positive, list_data)
    return list(seq_data)


def dictionary_screen(dict_data):
    new_dict_data = {}
    for key, value in dict_data.items():
        if value > 90:
            new_dict_data[key] = value
    return new_dict_data


def set_screen(set_data):
    new_set_data = set()
    for item in set_data:
        if item % 3 == 0:
            new_set_data.add(item)
    return new_set_data


if __name__ == '__main__':
    print(list_screen2([2, -5, 9, 3, -8]))
    print(dictionary_screen({'LiLei': 93, 'ZH': 82, 'Aryy': 120}))
    print(set_screen({1, 3, 5, 6}))
