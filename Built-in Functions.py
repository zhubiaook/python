'''
isinstance(object, classinfo)

'''

##############################

'''isinstance(object, classinfo)
Return true if the object argument is an instance of the classinfo argument, or of a (direct, indirect or virtual) subclass thereof. If object is not an object of the given type, the function always returns false. If classinfo is a tuple of type objects (or recursively, other such tuples), return true if object is an instance of any of the types. If classinfo is not a type or tuple of types and such tuples, a TypeError exception is raised.

isinstance() 用来判断一个对象是否是已知的文件类型，类似于type()

isinstance() 与 type()的区别：
	type() 不考虑继承，不会认为子类是一种父类型
	isinstance() 会认为子类是一种父类型
classinfo 可以是基本类型，直接或间接类名或由它们组成的元祖
'''

a = 2
#print(isinstance(a,int))
#print(isinstance(a,str))
#print(isinstance(a,(str,int,list)))

# type() 与 isinstance()区别
class A:
	pass
class B(A):
	pass

b = isinstance(A(),A)   #True
b = type(A()) == A      #True
b = isinstance(B(),A)   #True
b = type(B()) == A      #False

print(b)

