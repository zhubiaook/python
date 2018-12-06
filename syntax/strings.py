"""
DESCRIPTION
Version: 0.1
Author: slynxes
Date: 2018-12-03
"""


def main():
    str1 = 'Hello World!'

    # Return the length of the string
    # len(string)
    print(len(str1))

    # Capitalizes first letter of string
    # string.capitalize()
    print(str1.capitalize())

    # Converts lowercase letters in string to uppercase
    # string.upper()
    print(str1.upper())

    # Converts uppercase letters in string to lowercase
    # string.lower()
    str1.lower()

    # Determine if str occurs in string
    # string.find(str, beg, end)
    # 找到返回索引，否则返回=1
    print(str1.find('Wo', 1, len(str1)))

    # Same as find(), but raises an exception if str not found
    # string.index(str, beg, end)
    print(str1.index('Wo', 1, len(str1)))

    # Determine if string starts with substring str,
    # return true if so and false otherwise
    # string.startswith(str, beg, end)
    print(str1.startswith('He', 0, len(str1)))

    # Determine if string end with substring str,
    # return true if so and false otherwise
    # string.endswith(str, beg, end)
    print(str1.endswith('ld!', 0, len(str1)))

    # 返回一个指定宽度的字符串，字符串中央是原始字符串，两侧使用fillchar填充
    # string.center(width, fillchar)
    print(str1.center(50, '*'))

    # left-justified
    # string.ljust(width, fillchar)
    print(str1.ljust(20, 'o'))

    # right-justified
    # string.rjust(width, fillchar)
    print(str1.rjust(20, '0'))

    # string special operators
    print(str1[2:9])
    print(str1[:9])
    print(str1[5:])
    print(str1[-1])
    print(str1[0:-1])
    print(str1[0::2])
    print(str1[-5:])

    # Returns true if string contains only digits and false otherwise
    print(str1.isdigit())

    # Return true if string are alphabetic and false otherwise
    print(str1.isalpha())

    # Return turn if string are alphanumeric and false otherwise
    print(str1.isalnum())

    # Remove whitespace
    print(str1.strip())
    print(str1.lstrip())
    print(str1.rstrip())


if __name__ == '__main__':
    main()