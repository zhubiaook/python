'''元祖
1. 元祖与列表非常类似，不同之处在于元祖的元素是不可改变的
'''

# tuple祖赋值
t = 'a', 'b', 'c'
t = ('a', 'b', 'c')

# 单个元素赋值
t = 'a',

# 创建空元素元祖
t = tuple()

# 其序列转换为元祖
t = tuple('nice')
t = tuple(['a', 'b', 'c'])
t = tuple({'a':1, 'b':2, 'c':3})

# tuple 取值
e = t[0]
e = t[0:2]
e = t[:2]
e = t[:]
e = t[2:]

# tuple 比较, 首先从序列中的第一个元素开始比较，如果相等，继续往下比较，一旦比值不同，就完成比较，不会再比较后面的元素
(1,3,5) < (2,1,1)

# 使用 tuple 实现两个变量优雅的交换值
a = 5
b = 3
a,b = b,a #或(a,b) = (b,a)

# 元祖元素赋值
(a,b) = ['nice', 'good']
(a,b) = {'nice':1, 'good':2}
(a,b) = 'ni'

# split() 方法默认是对字符串按照空格进行分割
s = 'Hello world'
s = 'zhubiaook@outlook.com'
t = s.split('@') #指定分隔符
(a,b) = t

# divmod(num1,num2) Take two (non complex) numbers as arguments and return a pair of numbers consisting of their quotient and remainder when using integer division.
t = divmod(5,3)
quotient,remainder = divmod(5,3)

# 使用tuple作为函数的返回值，同时返回多个值
def min_max(num1,num2):
	if num1 < num2:
		min = num1
		max = num2
	else:
		min = num2
		max = num1
	return (min,max) # or return min,max


def print_all(*args):
	'''函数可以接受可变数量的形参
	所有传入的实参以tuple的形式保存在以 * 开头的变量中
	'''
	print(type(args))
	print(args)

#print_all(1,2,3,4)


def max_num(num1, num2):
	if num1 > num2:
		return num1
	else:
		return num2

t = [3,5]
max = max_num(*t) # 通常实参个数与形参个数相同，以 * 开头的变量可以传入多个实参


'''zip(*iterables)
Make an iterator that aggregates elements from each of the iterables.
Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables. The iterator stops when the shortest input iterable is exhausted. With a single iterable argument, it returns an iterator of 1-tuples. With no arguments, it returns an empty iterator. Equivalent to:
'''

def print_zip(*iterable):
	iter1, iter2 = iterable
	for pair in zip(iter1,iter2):
		print(pair)

#print_zip([1,3,5],[2,4,6])


def has_match(t1, t2):
	for x, y in zip(t1,t2):
		if x == y:
			return True
	return False

#print(has_match([1,3,5],[2,3,4]))


'''enumerate(iterable, start=0)
Return an enumerate object. iterable must be a sequence, an iterator, or some other object which supports iteration. The __next__() method of the iterator returned by enumerate() returns a tuple containing a count (from start which defaults to 0) and the values obtained from iterating over iterable.
'''

def print_enumerate(iterable):
	t = list(enumerate(iterable,start=1))
	return t

#print(print_enumerate(['ok','good','really']))


'''items()
Return a new view of the dictionary’s items ((key, value) pairs). See the documentation of view objects.
'''
# 字典转换成元祖列表
def print_items(d):
	for i in d.items():
		print(i)

d = {'one':1, 'two':2, 'three':3}
#print_items(d)

def make_list(t1,t2):
	t = list(zip(t1,t2))
	return t

# 元祖列表生成字典
def make_dict(t1,t2):
	d = dict(zip(t1,t2))
	return d

d = make_dict(['one','two','three'],['nice','good','great'])


# 使用 tuple 作为 dictionary 的 key
# dictionary 要求 key 是不可变类型，value 可以是任意类型

t1 = ['Cleese', 'Chapman', 'Idle', 'Gilliam']
t2 = ['John', 'Graham', 'Eric', 'Terry']
t3 = ['03700 100 222', '03700 100 222', '03700 100 222', '03700 100 222']
mt = make_list(t1,t2)
md = make_dict(mt,t3)

# tuple 不能像 list 一样使用方法 .sort() 进行排序，但可以使用 Built-in Functions sorted(), reversed() 进行排序
'''sorted()
sorted(iterable, *, key=None, reverse=False)
Return a new sorted list from the items in iterable.

Has two optional arguments which must be specified as keyword arguments.

key specifies a function of one argument that is used to extract a comparison key from each list element: key=str.lower. The default value is None (compare the elements directly).

reverse is a boolean value. If set to True, then the list elements are sorted as if each comparison were reversed.
'''
def tuple_sorted(t):
	result = tuple(sorted(t))
	return result


'''reversed(seq)
Return a reverse iterator. seq must be an object which has a __reversed__() method or supports the sequence protocol (the __len__() method and the __getitem__() method with integer arguments starting at 0).
'''

def tuple_reversed(seq):
	result = tuple(reversed(seq))
	return result

t = ('one','two','three')
print(tuple_reversed(t))


### END ###

