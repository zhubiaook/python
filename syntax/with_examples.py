class Foo():
    def __init__(self):
        print('Hello World')

    def __enter__(self):
        print('Good')

    def __exit__(self, type, value, trace):
        print('Haha')



def foo():
    return Foo()


with foo():
    pass

