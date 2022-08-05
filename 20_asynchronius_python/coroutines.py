#!/usr/bin/env python
from inspect import getgeneratorstate


# свой клас исключения
class BlaBlaException(Exception):
    pass

# декоратор инициализирует корутину
# для её готовности вызывает метод .send()
def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g

    return inner

# незадекорированная корутина
# изначально находится в статусе GEN_CREATED
def subgen():
    message = yield
    print(f"Subgen received: ", message)

# корутина с декоратором, который вызывает метод .send(None)
# что переводит корутину в статус GEN_SUSPENDED
@coroutine
def average():
    count = 0
    sum = 0
    average = None
    
    while True:
        try:
            x = yield average
        except StopIteration:
            print("Done")
            break
        except BlaBlaException:
            print("__________________________")
            break
        else:
            count += 1
            sum += x
            average = round(sum/count, 2)
            #print(average) # то что будет илдить каждую итерацию

    return average

def test():
    g = subgen()
    try:
        print(getgeneratorstate(g))
        #g.send("Ok ...") # TypeError: can't send non-None value to a just-started generator
        
        b = subgen()
        b.send(None)
        print(getgeneratorstate(b))
        b.send("Ok ...")

    except Exception as e:
        print(f"Мы поймали исключение: ",e)

def main():
    c = average()
    try:
        print(getgeneratorstate(c))
        c.send(5)
        c.send(4)
        c.send(9)
        c.throw(StopIteration) # метод .throw() может отправлять корутине исключение
    # таким способом мы можем его пойматьи возвратить return вне цикла event loop
    except StopIteration as e:
        print(e.value) # вызвав у исключения атрибут .value


if __name__ == '__main__':
    print("test def:\n")
    test()
    print("\nmain def:\n")
    main()