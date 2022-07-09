#!usr/bin/env python3

from functools import wraps


def suppress(errname, or_return=None):
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            try:
                func()
            except errname:
                print(f"Мы словили исключение {errname.__name__}, но успешно подавили его ¯\_(ツ)_/¯")
                print(or_return)
                return or_return
            except Exception as e:
                print(f"Мы словили исключение {e.__class__.__name__}, но успешно подавили его ¯\_(ツ)_/¯")
                print(or_return)
                return or_return
            else:
                print(or_return)
                return or_return
            finally:
                print("The END")
        return inner
    return wrapper

@suppress(ZeroDivisionError, or_return=42)
def foo():
    #raise ValueError
    return 1 // 0

def foo2():
    return 1 // 1

def test():
    
    foo()
    print(foo) # <function foo at 0x7f4393f7b0d0>

if __name__ == '__main__':
    test()