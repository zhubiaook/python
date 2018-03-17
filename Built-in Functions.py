'''
isinstance(object, classinfo)

'''

'''isinstance(object, classinfo)
Return true if the object argument is an instance of the classinfo argument, or of a (direct, indirect or virtual) subclass thereof. If object is not an object of the given type, the function always returns false. If classinfo is a tuple of type objects (or recursively, other such tuples), return true if object is an instance of any of the types. If classinfo is not a type or tuple of types and such tuples, a TypeError exception is raised.

classinfo 可以是基本类型，直接或间接类名或由它们组成的元祖
'''
